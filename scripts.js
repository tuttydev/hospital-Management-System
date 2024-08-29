document.addEventListener('DOMContentLoaded', function() {
    // Toggle dark mode
    const darkModeToggle = document.getElementById('darkModeToggle');
    darkModeToggle.addEventListener('change', function() {
        document.body.classList.toggle('dark-mode');
    });

    // Interactive sidebar links
    const sidebarLinks = document.querySelectorAll('.sidebar ul li a');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const sectionId = this.getAttribute('href').slice(1);
            scrollToSection(sectionId);
        });
    });

    // Function to scroll to a section
    function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (section) {
            window.scrollTo({
                top: section.offsetTop - 50,
                behavior: 'smooth'
            });
        }
    }

    // Animated content on page load
    const contentSections = document.querySelectorAll('.content-section');
    contentSections.forEach(section => {
        section.style.opacity = 0;
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });

    setTimeout(() => {
        contentSections.forEach(section => {
            section.style.opacity = 1;
            section.style.transform = 'translateY(0)';
        });
    }, 200);
});
