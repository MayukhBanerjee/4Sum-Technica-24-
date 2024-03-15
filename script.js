// let text = document.getElementById('text');
// let leaf = document.getElementById('leaf');
// let hill1 = document.getElementById('hill1');
// let hill4 = document.getElementById('hill4');
// let hill5 = document.getElementById('hill5');
// window.addEventListener ('scroll', () => {
//     let value = window.scrollY;
//     text.style.marginTop = value * 2.5 + "px";
//     leaf.style. top = value * -1.5 + 'px';
//     leaf.style.left = value * 1.5 + 'px';
//     hill5.style.left = value * 1.5 + "px";
//     hill4.style.left = value * -1.5 + "px";
//     hill1.style.top = value * 1 + 'px';

// })
// Selecting elements
// Selecting elements
// 
// Function to update element style based on scroll value
function updateElementStyle(element, property, valueMultiplier, unit = 'px') {
    element.style[property] = `${window.scrollY * valueMultiplier}${unit}`;
}

// Selecting elements
// const elements = {
//     text: document.getElementById('text'),
//     leaf: document.getElementById('leaf'),
//     hill1: document.getElementById('hill1'),
//     hill4: document.getElementById('hill4'),
//     hill5: document.getElementById('hill5')
// };

// // Event listener for scroll
// window.addEventListener('scroll', () => {
//     updateElementStyle(elements.text, 'marginTop', 2.5);
//     updateElementStyle(elements.leaf, 'top', -1.5);
//     updateElementStyle(elements.leaf, 'left', 1.5);
//     updateElementStyle(elements.hill1, 'top', 1);
//     updateElementStyle(elements.hill4, 'left', -1.5);
//     updateElementStyle(elements.hill5, 'left', 1.5);
// });
// Function to update element style based on scroll value
function updateElementStyle(element, property, valueMultiplier, unit = 'px') {
    element.style[property] = `${window.scrollY * valueMultiplier}${unit}`;
}
// Selecting elements
const elements = {
    text: document.getElementById('text'),
    leaf: document.getElementById('leaf'),
    hill1: document.getElementById('hill1'),
    hill4: document.getElementById('hill4'),
    hill5: document.getElementById('hill5')
};
// Event listener for scroll
window.addEventListener('scroll', () => {
    const value = window.scrollY;
    updateElementStyle(elements.text, 'marginTop', 2.5);
    updateElementStyle(elements.leaf, 'top', -1.5);
    updateElementStyle(elements.leaf, 'left', 1.5);
    updateElementStyle(elements.hill1, 'top', 1);
    updateElementStyle(elements.hill4, 'left', -2.5);
    updateElementStyle(elements.hill5, 'left', 1.5);
});



