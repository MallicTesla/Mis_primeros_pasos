window.addEventListener('DOMContentLoaded', (event) => {
    const menuLinks = document.querySelectorAll('.menu_list a');
    
    menuLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            menuLinks.forEach(link => {
                link.classList.remove('active');
            });
            event.target.classList.add('active');
        });
    });
});