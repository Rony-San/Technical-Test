async function fetchPopulationData(event) {
  event.preventDefault();

  try {
    const response = await fetch("/populations");
    const result = await response.json();

    if (result.status === "success") {
      const populationResults = document.getElementById("populationResults");
      const populationData = result.data.data
        .map(
          (item) =>
            `<p class="mt-4"><strong>Year:</strong> ${item["ID Year"]}, <strong>Population:</strong> ${item.Population}, <strong>Signed By:</strong> ${item.Signed}</p>`
        )
        .join("");
      populationResults.innerHTML = populationData;
    } else {
      alert("Error fetching data");
    }
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred while fetching the data.");
  }
}
