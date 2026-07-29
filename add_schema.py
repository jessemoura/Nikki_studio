import json
import re

schema = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.nikkistudio.co.uk/#organization",
      "name": "Nikki Studio",
      "url": "https://www.nikkistudio.co.uk",
      "logo": "https://www.nikkistudio.co.uk/assets/img/logo.png",
      "sameAs": [
        "https://www.instagram.com/nikki.studiouk",
        "https://www.snapchat.com/add/nikkixft"
      ]
    },
    {
      "@type": "LocalBusiness",
      "@id": "https://www.nikkistudio.co.uk/#localbusiness",
      "name": "Nikki Studio",
      "image": "https://www.nikkistudio.co.uk/assets/img/logo.png",
      "url": "https://www.nikkistudio.co.uk",
      "telephone": "+447305928322",
      "priceRange": "££",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "33 Mill View",
        "addressLocality": "West Swindon",
        "addressRegion": "Wiltshire",
        "postalCode": "SN5 4FN",
        "addressCountry": "UK"
      },
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00",
        "closes": "18:00"
      },
      "areaServed": {
        "@type": "City",
        "name": "Swindon"
      },
      "hasMap": "https://maps.google.com/?q=33+Mill+View,+Swindon,+SN5+4FN",
      "parentOrganization": {
        "@id": "https://www.nikkistudio.co.uk/#organization"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://www.nikkistudio.co.uk/#website",
      "url": "https://www.nikkistudio.co.uk",
      "name": "Nikki Studio | Acrylic Nails & Bespoke Nail Art in Swindon",
      "publisher": {
        "@id": "https://www.nikkistudio.co.uk/#organization"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.nikkistudio.co.uk/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How long does a full acrylic set take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Usually around 1.5 to 2 hours, depending on the complexity of the nail art and shape required. We don't rush, ensuring a perfect finish every time."
          }
        },
        {
          "@type": "Question",
          "name": "Do you remove work from other salons?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes! Please add a 'Soak-Off' to your booking so we can safely remove any previous product before applying your new set."
          }
        },
        {
          "@type": "Question",
          "name": "How do I pay?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "We accept cash and bank transfers at the studio. A small deposit may be required to secure your booking slot via WhatsApp."
          }
        },
        {
          "@type": "Question",
          "name": "Can I bring my own nail design ideas or inspiration images?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Absolutely! In fact, we highly encourage it. You can send us your favorite lifestyle images, Instagram clippings, or Pinterest pins directly over WhatsApp so we can customize your set perfectly."
          }
        },
        {
          "@type": "Question",
          "name": "How can I request a quote for custom nail designs?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our quote structure is fully transparent and based on your length preferences and the complexity of your intricate hand-painted nail art. You can request a precise, personalized custom quote directly on WhatsApp!"
          }
        },
        {
          "@type": "Question",
          "name": "Will acrylic nails or extensions damage my natural nails?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Not under our care. Damage is caused by hasty, aggressive drilling and force. We use ultra-gentle soaking methods, careful hand filing, and supportive hygiene to shield your natural nail health."
          }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.nikkistudio.co.uk/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://www.nikkistudio.co.uk"
        }
      ]
    }
  ]
}

services = [
    ("Acrylic Full Sets & Infills", "Custom length, shape and finish with full colour, French or custom designs, plus regular infill maintenance."),
    ("Classic French & Elegant Designs", "Timeless crisp tips, soft ombré and understated styles for everyday wear or special occasions."),
    ("Hand-Painted & 3D Nail Art", "Delicate florals, swirls, charms, pearls and 3D accents brought to life with detailed hand-painted work."),
    ("Pattern & Statement Nails", "Animal prints, bold lines, metallic details and themed unique designs."),
    ("Pedicure Treatments", "Relaxing foot care, cuticle work, gel polish finishes with optional gems and embellishments."),
    ("Safe Removal & Repair", "Gentle soak-off removal, conditioning and repairs to protect and restore natural nails.")
]

for name, desc in services:
    schema["@graph"].append({
      "@type": "Service",
      "name": name,
      "description": desc,
      "provider": {
        "@id": "https://www.nikkistudio.co.uk/#localbusiness"
      },
      "areaServed": {
        "@type": "City",
        "name": "Swindon"
      }
    })

script_tag = f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>\n</head>'

html_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('</head>', script_tag)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
