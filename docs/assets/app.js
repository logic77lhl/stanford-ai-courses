(function () {
  "use strict";

  // Mobile nav
  var menuBtn = document.getElementById("menuBtn");
  var nav = document.getElementById("nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      nav.classList.toggle("open");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.classList.remove("open");
    });
  }

  // Reveal on scroll
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });

    document.querySelectorAll(".section, .track, .poster-card, .path-card, .path-detail").forEach(function (el) {
      el.classList.add("reveal");
      io.observe(el);
    });
  }

  var grid = document.getElementById("courseGrid");
  if (!grid || !window.COURSES) return;

  var search = document.getElementById("courseSearch");
  var sort = document.getElementById("courseSort");
  var chips = Array.prototype.slice.call(document.querySelectorAll("#catChips .chip"));
  var typeButtons = Array.prototype.slice.call(document.querySelectorAll("#typeSeg button"));
  var countEl = document.getElementById("courseCount");
  var emptyEl = document.getElementById("courseEmpty");

  var state = { type: "all", cat: "all", q: "", sort: "code" };

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function stars(level) {
    if (!level) return "—";
    level = Math.max(1, Math.min(5, level));
    return "★".repeat(level) + "☆".repeat(5 - level);
  }

  function card(c) {
    var tags = (c.tags || []).slice(0, 3).map(function (t) {
      return "<span>" + esc(t) + "</span>";
    }).join("");
    var badge = c.type === "core" ? "核心" : "延伸";
    return '<a class="ccard" href="courses/' + esc(c.slug) + '.html" data-type="' + esc(c.type) + '">' +
      '<div class="ccard-top"><span class="ccard-code">' + esc(c.id) + "</span>" +
      '<span class="ccard-badge ' + (c.type === "ext" ? "ext" : "") + '">' + badge + "</span></div>" +
      "<h3>" + esc(c.zh) + "</h3><p>" + esc(c.card_desc || c.one) + "</p>" +
      '<div class="ccard-meta"><span>' + esc(c.terms) + '</span><span class="stars">' + stars(c.difficulty) + "</span></div>" +
      '<div class="ccard-tags">' + tags + "</div></a>";
  }

  function compare(a, b) {
    if (state.sort === "diff") return (b.difficulty || 0) - (a.difficulty || 0) || a.id.localeCompare(b.id, "en", { numeric: true });
    if (state.sort === "name") return a.zh.localeCompare(b.zh, "zh-Hans-CN");
    return a.id.localeCompare(b.id, "en", { numeric: true });
  }

  function render() {
    var q = state.q.trim().toLowerCase();
    var list = window.COURSES.filter(function (c) {
      if (state.type !== "all" && c.type !== state.type) return false;
      if (state.cat !== "all" && c.cat !== state.cat) return false;
      if (q && c.search.toLowerCase().indexOf(q) === -1) return false;
      return true;
    }).sort(compare);

    grid.innerHTML = list.map(card).join("");
    if (countEl) countEl.textContent = "共 " + list.length + " 门";
    if (emptyEl) emptyEl.hidden = list.length !== 0;
  }

  if (search) {
    search.addEventListener("input", function () {
      state.q = search.value;
      render();
    });
  }

  if (sort) {
    sort.addEventListener("change", function () {
      state.sort = sort.value;
      render();
    });
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      state.cat = chip.dataset.cat;
      chips.forEach(function (x) { x.classList.toggle("on", x === chip); });
      render();
    });
  });

  typeButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      state.type = btn.dataset.type;
      typeButtons.forEach(function (x) { x.classList.toggle("on", x === btn); });
      render();
    });
  });

  document.querySelectorAll(".track[data-filter]").forEach(function (track) {
    track.addEventListener("click", function () {
      state.cat = track.dataset.filter;
      chips.forEach(function (x) { x.classList.toggle("on", x.dataset.cat === state.cat); });
      render();
      var target = document.getElementById("courses");
      if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // "/" focuses search
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== search && search) {
      e.preventDefault();
      search.focus();
    }
  });

  render();
})();
