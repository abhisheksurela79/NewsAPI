const hamburgerIcon = document.querySelector(".hamburger-icon-container");
const CloseHamburgerIcon = document.querySelector(
  ".close-hamburger-icon-container"
);
const navLinks = document.querySelector(".nav-links");

hamburgerIcon.addEventListener("click", () => {
  hamburgerIcon.style.display = "none";
  CloseHamburgerIcon.style.display = "block";
  navLinks.style.display = "block";

  CloseHamburgerIcon.addEventListener("click", () => {
    CloseHamburgerIcon.style.display = "none";
    hamburgerIcon.style.display = "block";
    navLinks.style.display = "none";
  });
});

window.addEventListener("resize", () => {
  if (window.innerWidth >= 786) {
    hamburgerIcon.style.display = "none";
    CloseHamburgerIcon.style.display = "none";
    navLinks.style.display = "block";
  } else {
    CloseHamburgerIcon.style.display = "none";
    navLinks.style.display = "none";
    hamburgerIcon.style.display = "block";
  }
});

const navbar = document.querySelector("#nav");

window.addEventListener("scroll", (event) => {
    const navbarHeight = 60; // Set your initial navbar height
    const currentScrollPosition = window.scrollY;

    if (currentScrollPosition >= navbarHeight) {
        navbar.classList.add("sticky-navbar");
    } else {
        navbar.classList.remove("sticky-navbar");
    }
});

