document.addEventListener("DOMContentLoaded", function() {
  // Select all external links: Sphinx typically adds class="external" for them
  const externalLinks = document.querySelectorAll("a.external");

  externalLinks.forEach(link => {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
  });
});