//functionality for headers and footers
const burger_btn = document.querySelector(".options");
const header = document.querySelector("header")
const to_top = document.querySelector(".to-top")
const options_grey_area = document.querySelector(".options-back")

function toggle() {

    const on = burger_btn.classList.toggle('opts')
    const onn = header.classList.toggle('optionss')
}

if (to_top != null) {
    to_top.addEventListener('click', () => {
        window.scroll({ 'behavior': "smooth", 'top': 0 })
    })
}
// product click
// handles clicking
// functionality of every "product-card"
// no matter how the product card is designed


burger_btn.addEventListener('click', toggle)