(() => {
    window.onload = () => {
        const init_tooltips = () => $('[data-toggle="tooltip"]').tooltip();

        const init_creation_form_submit = () => {
            Cookies.set('_show_init_popup', 'false');
            const form = document.getElementById('gtm_demo_landing_creation_form');
            form.onsubmit = () => {
                Cookies.set('_show_init_popup', 'true');
            }
        }

        init_tooltips();
        init_creation_form_submit();
    };
})();