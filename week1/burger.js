function toggleMenu() {
    let popupMenu = document.getElementById("popupMenu");
    popupMenu.classList.toggle("active");
  }

function closeMenu() {
let popupMenu = document.getElementById("popupMenu");
popupMenu.classList.remove("active");
}


export {toggleMenu,closeMenu};