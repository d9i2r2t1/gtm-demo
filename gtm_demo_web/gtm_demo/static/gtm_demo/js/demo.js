(() => {
    window.onload = () => {
        const init_carousel = () => $('.carousel').carousel();

        const _push_to_datalayer = (event_name, category, action, label, extra_kwargs) => {
            window.dataLayer = window.dataLayer || [];
            const push_data = {
                'event': event_name,
                'category': category,
                'action': action,
                'label': label,
            }
            window.dataLayer.push(Object.assign({}, push_data, extra_kwargs));
        }

        const init_navbar_dl_pushes = () => {
            const navbar_buttons = [...document.getElementsByClassName('navbar-button')];
            navbar_buttons.forEach(elem => {
                elem.onclick = () => {
                    _push_to_datalayer('MenuSectionButtonClick', 'Navigation', 'Click menu', elem.textContent);
                }
            })
        }

        const init_login_button_df_push = () => {
            const login_button = document.getElementById('navbar-login-button');
            login_button.onclick = () => {
                _push_to_datalayer('MenuLoginButtonClick', 'Actions', 'Click menu', login_button.textContent);
            }
        }

        const init_login_form_submit = () => {
            const _is_login_valid = (event, element) => {
                if (element.value.match(/^student$/i) === null) {
                    _set_invalid_field(
                        event, element, 'LoginFormError', 'Errors', 'Form send', 'Login form: Логин не найден.'
                    );
                    return false;
                }
                return true;
            }
            const _is_pass_valid = (event, element) => {
                if (element.value.match(/^12345$/) === null) {
                    _set_invalid_field(
                        event, element, 'LoginFormError', 'Errors', 'Form send', 'Login form: Неверный пароль.'
                    );
                    return false;
                }
                return true;
            }
            const login_form = document.getElementById('login-form');
            login_form.onsubmit = (e) => {
                for (let element of [...login_form.elements]) {
                    if (element.id === 'login-form-login-field' && !_is_login_valid(e, element)) return;
                    if (element.id === 'login-form-pass-field' && !_is_pass_valid(e, element)) return;
                    element.classList.remove('is-invalid');
                }
                _push_to_datalayer('LoginFormSend', 'Actions', 'Form send', 'Login form');
            }
        }

        const _set_invalid_field = (event, element, ...dl_args) => {
            event.preventDefault();
            event.stopPropagation();
            element.classList.add('is-invalid');
            _push_to_datalayer(...dl_args);
        }

        const init_carousel_dl_pushes = () => {
            const carousel_buttons = [...document.getElementsByClassName('carousel-button')];
            carousel_buttons.forEach(elem => {
                elem.onclick = () => {
                    _push_to_datalayer('CarouselButtonClick', 'Actions', 'Carousel click', elem.textContent);
                }
            })
        }

        const init_buy_cards_dl_pushes = () => {
            const buy_buttons = [...document.getElementsByClassName('buy-button')];
            buy_buttons.forEach(elem => {
                elem.onclick = () => {
                    _push_to_datalayer('BuyButtonClick', 'Actions', 'Click buy button', elem.getAttribute('product'));
                }
            })
        }

        const init_buy_forms_submit = () => {
            const _is_tel_valid = (event, element, dl_label) => {
                if (element.value.match(/^(\+)?[0-9]+$/i) === null) {
                    _set_invalid_field(event, element, 'BuyFormError', 'Errors', 'Form send', dl_label);
                    return false;
                }
                return true;
            }
            const _is_card_valid = (event, element, dl_label) => {
                if (element.value.match(/^[0-9]{4,16}$/i) === null) {
                    _set_invalid_field(event, element, 'BuyFormError', 'Errors', 'Form send', dl_label);
                    return false;
                }
                return true;
            }
            const _is_data_check_valid = (event, element, dl_label) => {
                if (!element.checked) {
                    _set_invalid_field(event, element, 'BuyFormError', 'Errors', 'Form send', dl_label);
                    return false;
                }
                return true;
            }
            const buy_forms = [...document.getElementsByClassName('buy-subscription-form')];
            buy_forms.forEach(form => {
                form.onsubmit = (e) => {
                    for (let element of [...form.elements]) {
                        if (element.classList.contains('buy-form-tel-field') &&
                            !_is_tel_valid(e, element, form.getAttribute('product') + ' подписка: Некорректный номер телефона')) return;
                        if (element.classList.contains('buy-form-card-field') &&
                            !_is_card_valid(e, element, form.getAttribute('product') + ' подписка: Некорректный номер карты')) return;
                        if (element.classList.contains('buy-form-data-field') &&
                            !_is_data_check_valid(e, element, form.getAttribute('product') + ' подписка: Отсутствует согласие на обработку персональных данных')) return;
                        element.classList.remove('is-invalid');
                    }
                    _push_to_datalayer('BuyFormSend', 'Conversions', 'Form send', form.getAttribute('product') + ' подписка', {'price': form.getAttribute('price')});
                }
            });
        }

        const init_contacts_form_submit = () => {
            const contacts_form = document.getElementById('contacts-form');
            const submit_button = document.getElementById('contacts-form-submit-button');
            contacts_form.onsubmit = async (e) => {
                e.preventDefault();
                for (let element of [...contacts_form.elements]) {
                    element.value = '';
                }
                submit_button.classList.add('is-valid');
                _push_to_datalayer('ContactsFormSend', 'Conversions', 'Form send', 'Contacts form');
                await _disable_contacts_form_success_message();
            }
        }

        const _disable_contacts_form_success_message = async () => {
            const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
            await sleep(5000);
            document.getElementById('contacts-form-submit-button').classList.remove('is-valid');
        }

        const init_external_links_dl_pushes = () => {
            const external_links = [...document.getElementsByClassName('external-link')];
            external_links.forEach(elem => {
                elem.onclick = () => {
                    _push_to_datalayer('ExternalLinkClick', 'Actions', 'Click external link', elem.textContent);
                }
            })
        }

        const init_contacts_links_dl_pushes = () => {
            const contacts_links = [...document.getElementsByClassName('contacts-link')];
            contacts_links.forEach(elem => {
                elem.onclick = () => {
                    _push_to_datalayer('ContactsLinkClick', 'Actions', 'Click contacts link', elem.getAttribute('contacts_link_type'));
                }
            })
        }

        const show_init_popup = () => {
            if (Cookies.get('_show_init_popup') === 'true') {
                $('#welcome-modal').modal('show');
                Cookies.set('_show_init_popup', 'false');
            }
        }

        init_carousel();                  // Включаем карусель в демо-лендинге
        init_navbar_dl_pushes();          // Включаем пуши в dataLayer при кликах на кнопки меню
        init_login_button_df_push();      // Включаем пуш в dataLayer при клике на кнопку "Войти"
        init_login_form_submit();         // Включаем отслеживание отправки формы логина
        init_carousel_dl_pushes();        // Включаем пуши в dataLayer при кликах на кнопки карусели
        init_buy_cards_dl_pushes();       // Включаем пуши в dataLayer при кликах на кнопки "Купить"
        init_buy_forms_submit();          // Включаем отслеживание отправки форм покупок
        init_contacts_form_submit();      // Включаем отслеживание отправки формы контактов
        init_external_links_dl_pushes();  // Включаем пуши в dataLayer при кликах на внешние ссылки
        init_contacts_links_dl_pushes();  // Включаем пуши в dataLayer при кликах на ссылки в контактах
        show_init_popup();                // Активация попапа при первом открытии демо-лендинга
    };
})();