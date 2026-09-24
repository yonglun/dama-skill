const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const source = readFileSync(join(__dirname, "../dist/assets/site.js"), "utf8");

function loadPage(localStorage) {
  const document = {
    readyState: "complete",
    documentElement: { lang: "en" },
    querySelectorAll: () => [],
    querySelector: () => null,
    addEventListener: () => {},
  };
  const window = {};
  vm.runInNewContext(source, { document, window, localStorage });
  return { document, site: window.DamaSkillSite };
}

test("language choice survives navigation and page reload", () => {
  const values = new Map();
  const storage = {
    getItem: (key) => values.get(key) ?? null,
    setItem: (key, value) => values.set(key, value),
  };

  const first = loadPage(storage);
  assert.equal(first.site.state.language, "en");
  first.site.setLanguage("zh");
  assert.equal(first.document.documentElement.lang, "zh-CN");

  const returned = loadPage(storage);
  assert.equal(returned.site.state.language, "zh");
  assert.equal(returned.document.documentElement.lang, "zh-CN");

  returned.site.setLanguage("en");
  assert.equal(loadPage(storage).site.state.language, "en");
});

test("blocked browser storage does not break the language switch", () => {
  const blockedStorage = {
    getItem: () => { throw new Error("storage blocked"); },
    setItem: () => { throw new Error("storage blocked"); },
  };
  const page = loadPage(blockedStorage);
  assert.equal(page.site.state.language, "en");
  assert.equal(page.site.setLanguage("zh"), "zh");
  assert.equal(page.document.documentElement.lang, "zh-CN");
});

test("explicit language links in documentation update the homepage preference", () => {
  const docsSource = readFileSync(join(__dirname, "../dist/assets/docs-language.js"), "utf8");
  const values = new Map([["dama-data-project-skills-language", "zh"]]);
  const storage = {
    getItem: (key) => values.get(key) ?? null,
    setItem: (key, value) => values.set(key, value),
  };
  let clickHandler;
  const document = {
    addEventListener: (type, handler) => {
      if (type === "click") clickHandler = handler;
    },
  };
  const window = { location: { href: "http://127.0.0.1:8765/site-docs/v1.1.0/README.html", origin: "http://127.0.0.1:8765" } };
  vm.runInNewContext(docsSource, { document, window, localStorage: storage, URL });
  const follow = (href) => clickHandler({
    button: 0,
    target: { closest: () => ({ href }) },
  });

  follow("http://127.0.0.1:8765/site-docs/v1.1.0/README.en.html");
  assert.equal(values.get("dama-data-project-skills-language"), "en");
  follow("http://127.0.0.1:8765/index.html");
  assert.equal(values.get("dama-data-project-skills-language"), "en");
  follow("http://127.0.0.1:8765/site-docs/v1.1.0/skills/modeling-data/templates/delivery-pack.zh.html");
  assert.equal(values.get("dama-data-project-skills-language"), "zh");
  follow("https://other.example/README.en.html");
  assert.equal(values.get("dama-data-project-skills-language"), "zh");
});
