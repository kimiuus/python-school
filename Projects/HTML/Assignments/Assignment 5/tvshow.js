"use strict";

  const tvForm = document.querySelector("#tv-form");
  const DivRes = document.getElementById("results");
  tvForm.addEventListener("submit", async function (evt) {
    evt.preventDefault();
    const show = document.querySelector("input[name=q]").value;
    try {
      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${show}`);
      const jsonData = await response.json();
      DivRes.innerHTML = ""
for (const tvShow of jsonData) {
    const jsonShow = tvShow.show;

    const article = document.createElement("article");

    var br = document.createElement("br");

    const h2 = document.createElement("h2");
    h2.textContent = jsonShow.name;

    const a = document.createElement("a");
    a.href = jsonShow.url;
    a.textContent = "Details"
    a.target = "_blank";

    const img = document.createElement("img");
    img.src = jsonShow.image?.medium;
    img.alt = jsonShow.name;

    const summary = document.createElement("div");
    summary.innerHTML = jsonShow.summary;

    article.appendChild(h2);
    article.appendChild(img);
    article.appendChild(br);
    article.appendChild(a);
    article.appendChild(summary);
    DivRes.appendChild(article);

}


      console.log(jsonData);
    } catch (error) {
      console.log(error.message);
    }
  });