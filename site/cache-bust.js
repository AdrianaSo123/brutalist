// Force cache bust by appending version parameter
const version = Date.now();
document.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
    const href = link.getAttribute('href');
    if (!href.includes('?v=')) {
        link.setAttribute('href', href + '?v=' + version);
    }
});
