(() => {
  const cards = Array.from(document.querySelectorAll(".skill-card"));
  const groups = Array.from(document.querySelectorAll(".skill-group"));
  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const languageButtons = Array.from(document.querySelectorAll("[data-set-lang]"));
  const searchInput = document.querySelector("#skill-search");
  const resultsStatus = document.querySelector("#results-status");
  const emptyState = document.querySelector("#empty-state");
  const description = document.querySelector('meta[name="description"]');
  const validGroups = new Set(["all", "orchestration", "foundations", "delivery"]);
  const copy = {
    zh: {
      all: "显示全部 17 项技能",
      filtered: (count) => `筛选后显示 ${count} 项技能`,
      empty: "没有找到匹配项。试试其他关键词或清除筛选。",
      placeholder: "搜索技能、问题或产出…",
      description: "DAMA 数据项目技能套件：一个跨域路由入口与 16 个领域技能，支持团队按需组合并交付可验证成果。",
    },
    en: {
      all: "Showing all 17 skills",
      filtered: (count) => `Showing ${count} matching skills`,
      empty: "No skills match. Try another term or clear the filters.",
      placeholder: "Search skills, problems, or outputs…",
      description: "A bilingual suite of 17 DAMA-informed skills for planning and delivering data projects.",
    },
  };
  const state = { language: "en", group: "all", query: "" };

  function updateResultsStatus(count) {
    if (!resultsStatus) return;
    const languageCopy = copy[state.language];
    resultsStatus.textContent = state.group === "all" && state.query.length === 0
      ? languageCopy.all
      : languageCopy.filtered(count);
    if (emptyState) emptyState.hidden = count !== 0;
  }

  function filterSkills() {
    let visibleCount = 0;
    const query = state.query.trim().toLocaleLowerCase();

    cards.forEach((card) => {
      const matchesGroup = state.group === "all" || card.dataset.group === state.group;
      const searchableText = `${card.dataset.skill || ""} ${card.textContent || ""}`.toLocaleLowerCase();
      const matchesQuery = query.length === 0 || searchableText.includes(query);
      const visible = matchesGroup && matchesQuery;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    groups.forEach((group) => {
      const groupHasVisibleSkill = group.querySelector(".skill-card:not([hidden])") !== null;
      group.hidden = !groupHasVisibleSkill;
    });

    updateResultsStatus(visibleCount);
    return visibleCount;
  }

  function setGroup(group) {
    if (!validGroups.has(group)) return state.group;
    state.group = group;
    filterButtons.forEach((button) => {
      const selected = button.dataset.filter === state.group;
      button.classList.toggle("is-active", selected);
      button.setAttribute("aria-pressed", String(selected));
    });
    filterSkills();
    return state.group;
  }

  function setLanguage(language) {
    if (language !== "zh" && language !== "en") return state.language;
    state.language = language;
    document.documentElement.lang = language === "zh" ? "zh-CN" : "en";

    document.querySelectorAll("[data-lang]").forEach((element) => {
      element.hidden = element.dataset.lang !== language;
    });
    document.querySelectorAll("a[data-href-zh][data-href-en]").forEach((element) => {
      element.href = element.dataset[language === "zh" ? "hrefZh" : "hrefEn"];
    });
    document.querySelectorAll("[data-label-zh][data-label-en]").forEach((element) => {
      const labelKey = language === "zh" ? "labelZh" : "labelEn";
      element.setAttribute("aria-label", element.dataset[labelKey]);
    });
    document.querySelectorAll("img[data-alt-zh][data-alt-en]").forEach((image) => {
      image.alt = language === "zh" ? image.dataset.altZh : image.dataset.altEn;
    });
    languageButtons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.setLang === language));
    });
    if (searchInput) {
      searchInput.placeholder = copy[language].placeholder;
    }
    if (description) {
      description.content = copy[language].description;
    }
    filterSkills();
    return state.language;
  }

  function initializeDisclosures() {
    document.querySelectorAll(".example-toggle").forEach((button) => {
      const panel = document.getElementById(button.getAttribute("aria-controls"));
      if (!panel) return;
      panel.hidden = true;
      button.setAttribute("aria-expanded", "false");
      button.addEventListener("click", () => {
        const expanded = button.getAttribute("aria-expanded") !== "true";
        button.setAttribute("aria-expanded", String(expanded));
        panel.hidden = !expanded;
      });
    });
  }

  function initializeControls() {
    filterButtons.forEach((button) => {
      button.addEventListener("click", () => setGroup(button.dataset.filter));
    });
    languageButtons.forEach((button) => {
      button.addEventListener("click", () => setLanguage(button.dataset.setLang));
    });
    if (searchInput) {
      searchInput.addEventListener("input", () => {
        state.query = searchInput.value;
        filterSkills();
      });
    }
    document.addEventListener("keydown", (event) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLocaleLowerCase() === "k") {
        event.preventDefault();
        searchInput?.focus();
      }
      if (event.key === "Escape" && searchInput && searchInput.value) {
        searchInput.value = "";
        state.query = "";
        filterSkills();
      }
    });
  }

  function initialize() {
    initializeDisclosures();
    initializeControls();
    setLanguage(state.language);
    setGroup(state.group);
  }

  window.DamaSkillSite = {
    filterSkills,
    setGroup,
    setLanguage,
    get state() {
      return { ...state };
    },
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
