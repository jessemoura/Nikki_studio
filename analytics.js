/**
 * Nikki Studio — Commercial Analytics & UK GDPR/PECR Cookie Consent
 * Property GA4: G-PQKY693VH4
 */

(function () {
    'use strict';

    // 1. URL & PII Sanitization
    function sanitizeUrl(url) {
        if (!url) return window.location.origin + window.location.pathname;
        try {
            var parsed = new URL(url, window.location.origin);
            return parsed.origin + parsed.pathname;
        } catch (e) {
            return url.split('?')[0].split('#')[0];
        }
    }

    function sanitizeWhatsAppUrl(url) {
        if (!url) return 'https://wa.me/447305928322';
        try {
            var parsed = new URL(url, window.location.origin);
            // Return base wa.me path without pre-filled message text to protect PII
            return parsed.origin + parsed.pathname;
        } catch (e) {
            return 'https://wa.me/447305928322';
        }
    }

    function cleanText(text) {
        if (!text) return '';
        return text.replace(/\s+/g, ' ').trim();
    }

    // 2. Interaction Location Detection
    function getInteractionLocation(el) {
        if (!el) return 'page';
        if (el.closest('.whatsapp-pulse') || (el.getAttribute('aria-label') || '').toLowerCase().includes('contact nikki studio on whatsapp')) {
            return 'floating_button';
        }
        if (el.closest('header')) {
            var mobileMenu = el.closest('[x-show="mobileMenuOpen"]') || el.closest('#mobile-menu');
            return mobileMenu ? 'header_mobile' : 'header_desktop';
        }
        if (el.closest('#hero') || el.closest('section:first-of-type')) {
            return 'hero';
        }
        if (el.closest('#services')) {
            return 'services';
        }
        if (el.closest('#booking') || el.closest('form')) {
            return 'booking_form';
        }
        if (el.closest('#gallery')) {
            return 'gallery';
        }
        if (el.closest('#reviews')) {
            return 'reviews';
        }
        if (el.closest('#faq')) {
            return 'faq';
        }
        if (el.closest('footer')) {
            if (el.closest('ul')) return 'footer_contact';
            if (el.closest('.flex.items-center.gap-3')) return 'footer_social';
            return 'footer';
        }
        if (window.location.pathname.includes('/privacy')) {
            return 'privacy_page';
        }
        if (window.location.pathname.includes('/payment')) {
            return 'payment_page';
        }
        return 'main_content';
    }

    // 3. Debounce / Anti-Duplication Engine
    var clickCooldowns = new Map();
    function isDebounced(key, cooldownMs) {
        var now = Date.now();
        var last = clickCooldowns.get(key) || 0;
        if (now - last < (cooldownMs || 600)) {
            return true;
        }
        clickCooldowns.set(key, now);
        return false;
    }

    // 4. Safe GA4 Dispatcher
    function sendGa4Event(eventName, params) {
        if (typeof window.gtag === 'function') {
            window.gtag('event', eventName, params);
        }
        // Dispatch custom DOM event for testing / debugging
        window.dispatchEvent(new CustomEvent('nikki_ga4_event', {
            detail: { event: eventName, params: params }
        }));
    }

    // 5. Delegated Event Handlers
    function handleInteraction(target, isSubmit) {
        if (!target) return;

        var href = (target.getAttribute('href') || '').trim();
        var text = cleanText(target.innerText || target.getAttribute('aria-label') || '');
        var lowerText = text.toLowerCase();
        var lowerHref = href.toLowerCase();
        var location = getInteractionLocation(target);
        var pageLocation = sanitizeUrl(window.location.href);

        var isWhatsApp = lowerHref.includes('wa.me') || lowerHref.includes('whatsapp.com') || isSubmit || lowerText.includes('complete booking on whatsapp');
        var isInstagram = lowerHref.includes('instagram.com');
        var isFacebook = lowerHref.includes('facebook.com') || lowerHref.includes('fb.com');
        var isPhone = lowerHref.startsWith('tel:');
        var isBookNow = lowerText.includes('book now') ||
                        lowerText.includes('book your appointment') ||
                        lowerText.includes('book your set') ||
                        lowerText.includes('book service') ||
                        lowerText.includes('complete booking') ||
                        isSubmit;

        // WhatsApp Event
        if (isWhatsApp) {
            var waKey = 'wa_' + location + '_' + text;
            if (!isDebounced(waKey, 600)) {
                sendGa4Event('whatsapp_click', {
                    'page_location': pageLocation,
                    'link_url': sanitizeWhatsAppUrl(href),
                    'link_text': text || 'WhatsApp',
                    'interaction_location': location
                });
            }
        }

        // Instagram Event
        if (isInstagram) {
            var igKey = 'ig_' + location + '_' + href;
            if (!isDebounced(igKey, 600)) {
                sendGa4Event('instagram_click', {
                    'page_location': pageLocation,
                    'link_url': href,
                    'link_text': text || 'Instagram',
                    'interaction_location': location
                });
            }
        }

        // Facebook Event (prepared for present and future links)
        if (isFacebook) {
            var fbKey = 'fb_' + location + '_' + href;
            if (!isDebounced(fbKey, 600)) {
                sendGa4Event('facebook_click', {
                    'page_location': pageLocation,
                    'link_url': href,
                    'link_text': text || 'Facebook',
                    'interaction_location': location
                });
            }
        }

        // Phone Click Event (tel: links)
        if (isPhone) {
            var phoneKey = 'phone_' + location + '_' + href;
            if (!isDebounced(phoneKey, 600)) {
                sendGa4Event('phone_click', {
                    'page_location': pageLocation,
                    'link_url': href,
                    'link_text': text || 'Phone',
                    'interaction_location': location
                });
            }
        }

        // Book Now Click Event
        if (isBookNow) {
            var bookKey = 'book_' + location + '_' + text;
            if (!isDebounced(bookKey, 600)) {
                sendGa4Event('book_now_click', {
                    'page_location': pageLocation,
                    'link_url': href ? (lowerHref.includes('wa.me') ? sanitizeWhatsAppUrl(href) : href) : pageLocation + '#booking',
                    'link_text': text || 'Book Now',
                    'interaction_location': location
                });
            }
        }
    }

    // Attach Click Listener
    document.addEventListener('click', function (e) {
        var el = e.target.closest('a, button, [role="button"], input[type="submit"]');
        if (el) {
            handleInteraction(el, false);
        }
    }, true);

    // Attach Form Submit Listener (for keyboard Enter or form submit)
    document.addEventListener('submit', function (e) {
        var form = e.target;
        var submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
        handleInteraction(submitBtn || form, true);
    }, true);

    // 6. UK GDPR / PECR Cookie Consent System (Google Consent Mode v2)
    function applyConsent(granted) {
        var status = granted ? 'granted' : 'denied';
        localStorage.setItem('nikki_cookie_consent', status);
        if (typeof window.gtag === 'function') {
            window.gtag('consent', 'update', {
                'analytics_storage': status
            });
        }
        var banner = document.getElementById('nikki-cookie-banner');
        if (banner) {
            banner.style.opacity = '0';
            banner.style.transform = 'translateY(20px)';
            setTimeout(function () {
                if (banner && banner.parentNode) {
                    banner.style.display = 'none';
                }
            }, 300);
        }
    }

    function renderCookieBanner() {
        if (document.getElementById('nikki-cookie-banner')) {
            var existing = document.getElementById('nikki-cookie-banner');
            existing.style.display = 'block';
            setTimeout(function () {
                existing.style.opacity = '1';
                existing.style.transform = 'translateY(0)';
            }, 10);
            return;
        }

        var banner = document.createElement('div');
        banner.id = 'nikki-cookie-banner';
        banner.setAttribute('role', 'dialog');
        banner.setAttribute('aria-label', 'Cookie Preferences');
        banner.style.cssText = 'position:fixed;bottom:20px;left:20px;right:20px;max-width:440px;margin-left:auto;z-index:99999;transition:all 0.3s cubic-bezier(0.16, 1, 0.3, 1);opacity:0;transform:translateY(20px);';

        var privacyUrl = window.location.pathname.includes('/privacy') ? '#' : (window.location.pathname.includes('/payment') ? '../privacy/index.html' : 'privacy/index.html');

        banner.innerHTML = `
            <div class="bg-white dark:bg-[#18181b] text-gray-800 dark:text-gray-100 p-6 rounded-3xl shadow-2xl border border-pink-100 dark:border-gray-800 text-sm">
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xl">🍪</span>
                    <h3 class="font-serif font-bold text-base text-gray-900 dark:text-white">Cookie Preferences</h3>
                </div>
                <p class="text-xs text-gray-600 dark:text-gray-300 leading-relaxed mb-4">
                    We use essential storage to remember your visual theme and optional Google Analytics cookies to improve our studio appointment experience. Under UK GDPR/PECR, you choose how your data is used.
                    <a href="${privacyUrl}" class="text-[#FF4FA3] hover:underline ml-1">Privacy Policy</a>
                </p>
                <div class="flex flex-col sm:flex-row gap-2.5">
                    <button id="nikki-cookie-accept" type="button" class="flex-1 bg-[#FF4FA3] hover:bg-[#e03d8f] text-white py-2.5 px-4 rounded-xl font-medium text-xs text-center transition-colors shadow-sm focus:outline-none focus:ring-2 focus:ring-[#FF4FA3]">
                        Accept All
                    </button>
                    <button id="nikki-cookie-reject" type="button" class="flex-1 bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 text-gray-800 dark:text-gray-200 py-2.5 px-4 rounded-xl font-medium text-xs text-center transition-colors border border-gray-200 dark:border-gray-700 focus:outline-none">
                        Essential Only
                    </button>
                </div>
            </div>
        `;

        document.body.appendChild(banner);

        setTimeout(function () {
            banner.style.opacity = '1';
            banner.style.transform = 'translateY(0)';
        }, 50);

        document.getElementById('nikki-cookie-accept').addEventListener('click', function () {
            applyConsent(true);
        });

        document.getElementById('nikki-cookie-reject').addEventListener('click', function () {
            applyConsent(false);
        });
    }

    // Expose Cookie Settings opener globally for footer links
    window.openNikkiCookieSettings = function () {
        renderCookieBanner();
    };

    // Auto-init banner if consent is not determined yet
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            if (localStorage.getItem('nikki_cookie_consent') === null) {
                renderCookieBanner();
            }
        });
    } else {
        if (localStorage.getItem('nikki_cookie_consent') === null) {
            renderCookieBanner();
        }
    }

})();
