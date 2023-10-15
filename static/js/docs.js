const baseUrl = document.querySelector(".domain-name");
baseUrl.innerHTML = window.location.origin;

// Get references to the button and the dropdown menu
const countryButtonDropdown = document.querySelector(
  ".country-button-dropdown"
);
const countryDropdownMenu = document.querySelector(".country-dropdown-menu");
const countryDropdownItem = document.querySelectorAll(".country-dropdown-item");

// Initially hide the dropdown menu
countryDropdownMenu.style.display = "none";

// Toggle the dropdown menu's visibility when the button is clicked
countryButtonDropdown.addEventListener("click", () => {
  countryDropdownItem.forEach((option) => {
    option.addEventListener("click", () => {
      countryButtonDropdown.innerHTML = option.dataset.countryCode;
      countryDropdownMenu.style.display = "none";
    });
  });

  if (
    countryDropdownMenu.style.display === "none" ||
    countryDropdownMenu.style.display === ""
  ) {
    // Show the dropdown menu
    countryDropdownMenu.style.display = "block";
  } else {
    // Hide the dropdown menu
    countryDropdownMenu.style.display = "none";
  }
});

// Close the dropdown menu if the user clicks outside of it
document.addEventListener("click", (event) => {
  if (
    !countryButtonDropdown.contains(event.target) &&
    !countryDropdownMenu.contains(event.target)
  ) {
    countryDropdownMenu.style.display = "none";
  }
});

// Get references to the button and the dropdown menu
const categoryButtonDropdown = document.querySelector(
  ".category-button-dropdown"
);
const categoryDropdownMenu = document.querySelector(".category-dropdown-menu");
const categoryDropdownItem = document.querySelectorAll(
  ".category-dropdown-item"
);

// Initially hide the dropdown menu
categoryDropdownMenu.style.display = "none";

// Toggle the dropdown menu's visibility when the button is clicked
categoryButtonDropdown.addEventListener("click", () => {
  categoryDropdownItem.forEach((option) => {
    option.addEventListener("click", () => {
      categoryButtonDropdown.innerHTML = option.dataset.categoryCode;
      categoryDropdownMenu.style.display = "none";
    });
  });

  if (
    categoryDropdownMenu.style.display === "none" ||
    categoryDropdownMenu.style.display === ""
  ) {
    // Show the dropdown menu
    categoryDropdownMenu.style.display = "block";
  } else {
    // Hide the dropdown menu
    categoryDropdownMenu.style.display = "none";
  }
});

// Close the dropdown menu if the user clicks outside of it
document.addEventListener("click", (event) => {
  if (
    !categoryButtonDropdown.contains(event.target) &&
    !categoryDropdownMenu.contains(event.target)
  ) {
    categoryDropdownMenu.style.display = "none";
  }
});

const pageSizePara = document.querySelector(".page-size-container > p");
const pageSizeInput = document.querySelector(".page-size-container > input");

pageSizePara.addEventListener("click", () => {
  pageSizePara.style.display = "none";
  pageSizeInput.style.display = "block";

  pageSizeInput.addEventListener("input", (event) => {
    if (Number(pageSizeInput.value) === 0) {
      pageSizeInput.value = 1;
      pageSizePara.innerHTML = 1;
    } else {
      pageSizePara.innerHTML = pageSizeInput.value;
    }
  });
});

document.addEventListener("click", (event) => {
  if (
    !pageSizePara.contains(event.target) &&
    !pageSizeInput.contains(event.target)
  ) {
    pageSizePara.style.display = "block";
    pageSizeInput.style.display = "none";
  }
});

const pageNumberPara = document.querySelector(".page-number-container > p");
const pageNumberInput = document.querySelector(
  ".page-number-container > input"
);

pageNumberPara.addEventListener("click", () => {
  pageNumberPara.style.display = "none";
  pageNumberInput.style.display = "block";

  pageNumberInput.addEventListener("input", (event) => {
    if (Number(pageNumberInput.value) === 0) {
      pageNumberInput.value = 1;
      pageNumberPara.innerHTML = 1;
    } else {
      pageNumberPara.innerHTML = pageNumberInput.value;
    }
  });
});

document.addEventListener("click", (event) => {
  if (
    !pageNumberPara.contains(event.target) &&
    !pageNumberInput.contains(event.target)
  ) {
    pageNumberPara.style.display = "block";
    pageNumberInput.style.display = "none";
  }
});

//

const codeElement = document.querySelector(".api-response-section");
const jsonCodeElement = document.querySelector(".api-response-section code");
const fetchButton = document.querySelector(".fetch-button");

// Function to convert URLs in the JSON to clickable links
function formatJSONStringToHTML(text) {
  const urlRegex = /https?:\/\/[^\s/$.?#].[^\s]*/g;
  codeElement.style.display = "block";

  const formattedJson = text.replace(
    /(".*?":)/g,
    '<span class="key">$1</span>'
  );

  return formattedJson.replace(urlRegex, (url) => {
    return `<a href="${url}" target="_blank">${url}</a>`;
  });
}

fetchButton.addEventListener("click", () => {
  let country_code = document.querySelector(
    ".country-button-dropdown"
  ).innerHTML;
  let category = document.querySelector(".category-button-dropdown").innerHTML;
  let page = document.querySelector(".page-number-container > p").innerHTML;
  let pageSize = document.querySelector(".page-size-container > p").innerHTML;

  let url = `${window.location.origin}/api/?country_code=${country_code}&category=${category}&page=${page}&page_size=${pageSize}`;

  // Fetch JSON data from the API
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      // Convert the JSON data to a formatted string and replace URLs with links
      const formattedData = JSON.stringify(data, null, 10);

      const formatToHTML = formatJSONStringToHTML(formattedData);

      // Set the content of the <code> element with links
      jsonCodeElement.innerHTML = formatToHTML;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});

const openLink = document.querySelector(".open-fetch-response-button");

openLink.addEventListener("click", () => {

  let country_code = document.querySelector(".country-button-dropdown").innerHTML;
  let category = document.querySelector(".category-button-dropdown").innerHTML;
  let page = document.querySelector(".page-number-container > p").innerHTML;
  let pageSize = document.querySelector(".page-size-container > p").innerHTML;

  let url = `${window.location.origin}/api/?country_code=${country_code}&category=${category}&page=${page}&page_size=${pageSize}&format=json`;
  
  window.open(url, "_blank");
});