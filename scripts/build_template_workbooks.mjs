#!/usr/bin/env node
/** Generate the bilingual register workbooks from the validated catalog. */
import fs from "node:fs/promises";
import path from "node:path";

const moduleName = process.env.DAMA_ARTIFACT_TOOL_MODULE || "@oai/artifact-tool";
const { SpreadsheetFile, Workbook } = await import(moduleName);
const source = JSON.parse(await fs.readFile(process.argv[2], "utf8"));
const { catalog, skills_root: skillsRoot } = source;
const previewRoot = process.env.DAMA_TEMPLATE_PREVIEW_DIR;
const previewSkill = process.env.DAMA_TEMPLATE_PREVIEW_SKILL;

function columnLetter(index) {
  let number = index + 1;
  let result = "";
  while (number) {
    number -= 1;
    result = String.fromCharCode(65 + (number % 26)) + result;
    number = Math.floor(number / 26);
  }
  return result;
}

for (const [slug, spec] of Object.entries(catalog.skills).sort(([a], [b]) => a.localeCompare(b))) {
  for (const lang of ["zh", "en"]) {
    const workbook = Workbook.create();
    const guide = workbook.worksheets.add(lang === "zh" ? "说明" : "Instructions");
    guide.showGridLines = false;
    guide.getRange("A1:B1").values = [[spec.register_title[lang], slug]];
    guide.getRange("A1:B1").format = {
      fill: "#171717", font: { name: "Arial", bold: true, color: "#FFFFFF", size: 13 },
    };
    guide.getRange("A:B").format.columnWidth = 35;
    guide.getRange("B:B").format.columnWidth = 76;
    let row = 3;
    guide.getRange(`A${row}:B${row}`).values = [[lang === "zh" ? "字段 / ID" : "Field / ID", lang === "zh" ? "填写说明" : "Entry guidance"]];
    guide.getRange(`A${row}:B${row}`).format = {
      fill: "#D9E8EF", font: { name: "Arial", bold: true, color: "#171717" },
    };
    row += 1;
    for (const field of catalog.common_fields) {
      guide.getRange(`A${row}:B${row}`).values = [[`${field[lang]} · ${field.id}`, ""]];
      row += 1;
    }
    for (const sheetSpec of spec.sheets) {
      row += 1;
      guide.getRange(`A${row}:B${row}`).values = [[`${sheetSpec.name[lang]} · ${sheetSpec.id}`, sheetSpec.purpose[lang]]];
      guide.getRange(`A${row}:B${row}`).format = {
        fill: "#D9E8EF", font: { name: "Arial", bold: true, color: "#171717" },
      };
      row += 1;
      for (const column of sheetSpec.columns) {
        guide.getRange(`A${row}:B${row}`).values = [[`${column[lang]} · ${column.id}`, column.instruction[lang]]];
        row += 1;
      }
    }
    guide.getRange(`A1:B${row}`).format.font.name = "Arial";
    guide.getRange(`A1:B${row}`).format.wrapText = true;
    guide.freezePanes.freezeRows(3);

    for (const [index, sheetSpec] of spec.sheets.entries()) {
      const sheet = workbook.worksheets.add(sheetSpec.name[lang]);
      sheet.showGridLines = false;
      const last = columnLetter(sheetSpec.columns.length - 1);
      sheet.getRange(`A1:${last}1`).values = [sheetSpec.columns.map(column => `${column[lang]} · ${column.id}`)];
      sheet.getRange(`A1:${last}1`).format = {
        fill: "#171717", font: { name: "Arial", bold: true, color: "#FFFFFF", size: 10 },
      };
      sheet.getRange(`A1:${last}1`).format.rowHeight = 32;
      sheet.getRange(`A1:${last}26`).format.wrapText = true;
      sheet.getRange(`A:${last}`).format.columnWidth = 23;
      sheet.freezePanes.freezeRows(1);
      const table = sheet.tables.add(`A1:${last}26`, true, `Register_${index + 1}`);
      table.style = "TableStyleMedium2";
      table.showFilterButton = true;
    }
    workbook.recalculate();
    if (previewRoot && (!previewSkill || previewSkill === slug)) {
      for (const sheet of workbook.worksheets.items) {
        const preview = await workbook.render({ sheetName: sheet.name, range: "A1:F12", scale: 0.8, format: "png" });
        const folder = path.join(previewRoot, slug, lang);
        await fs.mkdir(folder, { recursive: true });
        await fs.writeFile(path.join(folder, `${sheet.name}.png`), new Uint8Array(await preview.arrayBuffer()));
      }
    }
    const output = path.join(skillsRoot, slug, "templates", `register.${lang}.xlsx`);
    const file = await SpreadsheetFile.exportXlsx(workbook);
    await file.save(output);
    await fs.unlink(`${output}.inspect.ndjson`).catch(error => {
      if (error.code !== "ENOENT") throw error;
    });
  }
}
