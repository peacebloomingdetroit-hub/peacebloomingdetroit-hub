/* Peace Blooming — minimal site JS */

(function () {
    'use strict';

    // Mobile nav toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function () {
            const expanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', String(!expanded));
            navMenu.classList.toggle('is-open');
            document.body.classList.toggle('nav-open');
        });

        // Close menu when a link is clicked
        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('is-open');
                document.body.classList.remove('nav-open');
            });
        });
    }

    // Sticky CTA: hide when footer is in view, show otherwise
    const stickyCta = document.querySelector('.sticky-cta');
    const footer = document.querySelector('footer');

    if (stickyCta && footer && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    stickyCta.classList.add('is-hidden');
                } else {
                    stickyCta.classList.remove('is-hidden');
                }
            });
        }, { threshold: 0.1 });

        observer.observe(footer);
    }

    // Contact form success message
    const formSuccess = document.getElementById('form-success');
    const serviceForm = document.getElementById('service-request');
    if (formSuccess && serviceForm) {
        const params = new URLSearchParams(window.location.search);
        if (params.get('success') === '1') {
            formSuccess.removeAttribute('hidden');
            serviceForm.setAttribute('hidden', '');
        }
    }

    // Client-side validation helpers
    const contactInput = document.getElementById('contact');
    if (contactInput) {
        contactInput.addEventListener('blur', function () {
            const value = this.value.trim();
            const hasPhone = /\d{3}/.test(value);
            const hasEmail = value.includes('@') && /.+@.+\..+/.test(value);
            this.setCustomValidity((hasPhone || hasEmail) ? '' : 'Please enter a valid phone number or email address');
        });
    }

    // Newsletter signup success message
    const newsletterForm = document.querySelector('form[name="newsletter"]');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function () {
            newsletterForm.classList.add('is-submitting');
        });
    }
})();
