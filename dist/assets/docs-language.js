(() => {
  const languagePreferenceKey = "dama-data-project-skills-language";

  document.addEventListener("click", (event) => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target?.closest?.("a[href]");
    if (!link) return;

    const target = new URL(link.href, window.location.href);
    if (target.origin !== window.location.origin) return;
    const language = target.pathname.endsWith("/README.html") || target.pathname.endsWith(".zh.html")
      ? "zh"
      : target.pathname.endsWith(".en.html") ? "en" : null;
    if (!language) return;

    try {
      localStorage.setItem(languagePreferenceKey, language);
    } catch {
      // Documentation links still work when browser storage is unavailable.
    }
  });
})();
