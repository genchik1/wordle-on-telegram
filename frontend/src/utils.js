export const cssVar = (name) => getComputedStyle(document.documentElement).getPropertyValue(name).trim();
