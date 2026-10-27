#!/usr/bin/env python3
"""Static site for Saha Express – pharmacy & errand delivery in Tangier (FR / AR / EN)."""
import json, html, shutil
from urllib.parse import quote
from pathlib import Path
OUT = Path(__file__).parent / "docs"
URL = "https://www.sahaexpresstanger.com"
INDEXNOW_KEY = "5a7e2c9d41b84f0f9c3e6a1b8d2f7e40"
WA = "212689302303"; SRC = "\n\n🌐 sahaexpresstanger.com"; TEL = "+212689302303"; TEL_SHOW = "06 89 30 23 03"
e = html.escape
ZONES = ["Malabata", "Branes", "Iberia", "Californie", "Najma", "Jbel Kbir", "Marshan", "Médina", "Kasbah", "Centre-ville",
         "Boulevard Pasteur", "Val Fleuri", "Mesnana", "Achakar", "Beni Makada", "Casabarata", "Dradeb", "Mghogha",
         "Bir Chifa", "Souani", "Moujahidine", "Hay Mohammadi", "Charf", "Msallah", "Boukhalef", "Gzenaya", "Rmilat", "Tanja Balia"]

T = {
"fr": dict(dir="ltr", path="", name="Français",
 alt_night="Livreur Saha Express la nuit à Tanger devant une pharmacie",
 open="Ouvert 24h/24", band_t="Besoin d'un médicament maintenant ?", band_p="Envoyez votre ordonnance, on s'occupe du reste. Partout à Tanger, jour et nuit.",
 title="Livraison pharmacie de garde à Tanger 24h/24 | Saha Express",
 desc="Saha Express récupère vos médicaments à la pharmacie de garde et vous les livre partout à Tanger, jour et nuit. Envoyez votre ordonnance sur WhatsApp. À partir de 20 DH.",
 kicker="Tanger · 24h/24 · 7j/7", h1="Vos médicaments livrés chez vous, <span>même la nuit</span>",
 lead="Malade, avec un enfant, ou sans voiture ? Envoyez-nous votre ordonnance sur WhatsApp. Nous allons à la pharmacie de garde ouverte et nous vous livrons à domicile, partout à Tanger.",
 cta="Envoyer mon ordonnance", call="Appeler", price="Livraison à partir de", dh="DH",
 chips=["🌙 Jour et nuit", "📍 Tout Tanger", "📄 Ordonnance sur WhatsApp", "💵 Paiement à la livraison"],
 how_t="Comment ça marche ?", how=[("📸","Envoyez votre ordonnance","Prenez une photo de l'ordonnance (ou écrivez le nom du produit) et envoyez-la sur WhatsApp avec votre adresse."),("🏥","Nous allons à la pharmacie","Nous trouvons la pharmacie de garde ouverte et nous vous confirmons le prix des médicaments avant d'acheter."),("🛵","Livraison chez vous","Le livreur vous apporte la commande. Vous payez les médicaments et la livraison à la réception.")],
 form_t="Commander maintenant", f_name="Votre prénom", f_zone="Quartier", f_addr="Adresse et repère", f_note="Médicaments ou remarque (facultatif)",
 f_send="Envoyer sur WhatsApp", f_hint="WhatsApp s'ouvre avec votre message prêt. Ajoutez ensuite la photo de l'ordonnance.",
 wa_hello="Bonjour Saha Express, je voudrais une livraison de pharmacie.", wa_name="Prénom", wa_zone="Quartier", wa_addr="Adresse", wa_note="Remarque", wa_photo="Je vous envoie la photo de l'ordonnance.",
 more_t="Pas seulement la pharmacie", more="Nous livrons aussi vos courses, repas, documents et colis partout à Tanger.",
 zones_t="Nous livrons dans tous les quartiers de Tanger", zones_note="Votre quartier n'est pas dans la liste ? Nous livrons quand même partout à Tanger — écrivez-nous.",
 rules_t="Important", rules=["Saha Express est un service de livraison, pas une pharmacie. Les médicaments sont achetés dans une pharmacie agréée.","Pour les médicaments sur ordonnance, l'ordonnance est obligatoire.","Nous ne donnons pas de conseils médicaux. En cas d'urgence, appelez le 15 (SAMU) ou le 150."],
 faq_t="Questions fréquentes", faq=[("Combien coûte la livraison ?","La livraison commence à 20 DH. Le prix exact dépend de la distance ; nous vous le confirmons sur WhatsApp avant de partir."),("Vous livrez la nuit ?","Oui, nous livrons 24h/24 et 7j/7, y compris la nuit et le week-end, depuis la pharmacie de garde ouverte."),("Comment je paie ?","Vous payez en espèces à la réception : le prix des médicaments (ticket de la pharmacie) plus la livraison."),("Faut-il une ordonnance ?","Oui pour les médicaments sur ordonnance. Pour les autres produits (para-pharmacie, bébé…), envoyez simplement le nom."),("Quels quartiers ?","Tout Tanger : Malabata, Branes, Iberia, Californie, Najma, Jbel Kbir, Mesnana, Beni Makada et tous les autres.")],
 guide_t="Pharmacie de garde à Tanger la nuit : que faire ?", guide_l="Lire le guide",
 foot="Saha Express – livraison à Tanger", legal="Service de livraison. Saha Express n'est pas une pharmacie et ne vend pas de médicaments."),
"ar": dict(dir="rtl", path="ar/", name="العربية",
 alt_night="موزع Saha Express ليلاً في طنجة أمام صيدلية",
 open="مفتوح 24/24", band_t="تحتاج دواءً الآن؟", band_p="أرسل الوصفة ونحن نتكفّل بالباقي. في كل طنجة، ليلاً ونهاراً.",
 title="توصيل الأدوية من صيدلية الحراسة في طنجة 24/24 | Saha Express",
 desc="نجلب لك الدواء من صيدلية الحراسة ونوصله إلى باب بيتك في كل أحياء طنجة، ليلاً ونهاراً. أرسل الوصفة على واتساب. التوصيل ابتداءً من 20 درهم.",
 kicker="طنجة · 24/24 · كل أيام الأسبوع", h1="دواؤك يصلك إلى البيت، <span>حتى في الليل</span>",
 lead="مريض، أو مع طفل، أو بدون سيارة؟ أرسل لنا الوصفة على واتساب. نذهب إلى صيدلية الحراسة المفتوحة ونوصل لك الدواء إلى البيت، في كل طنجة.",
 cta="أرسل الوصفة", call="اتصل", price="التوصيل ابتداءً من", dh="درهم",
 chips=["🌙 ليلاً ونهاراً", "📍 كل طنجة", "📄 الوصفة على واتساب", "💵 الدفع عند الاستلام"],
 how_t="كيف نعمل؟", how=[("📸","أرسل الوصفة","صوّر الوصفة (أو اكتب اسم الدواء) وأرسلها على واتساب مع عنوانك."),("🏥","نذهب إلى الصيدلية","نجد صيدلية الحراسة المفتوحة ونؤكد لك ثمن الدواء قبل الشراء."),("🛵","نوصله إلى بيتك","يصلك الموزع بالطلب، وتدفع ثمن الدواء والتوصيل عند الاستلام.")],
 form_t="اطلب الآن", f_name="اسمك", f_zone="الحي", f_addr="العنوان وعلامة قريبة", f_note="الدواء أو ملاحظة (اختياري)",
 f_send="أرسل على واتساب", f_hint="سيفتح واتساب برسالة جاهزة. بعدها أرسل صورة الوصفة.",
 wa_hello="السلام عليكم Saha Express، أريد توصيل دواء من الصيدلية.", wa_name="الاسم", wa_zone="الحي", wa_addr="العنوان", wa_note="ملاحظة", wa_photo="سأرسل لكم صورة الوصفة.",
 more_t="ليس الدواء فقط", more="نوصل أيضاً المشتريات والوجبات والوثائق والطرود في كل طنجة.",
 zones_t="نوصل إلى كل أحياء طنجة", zones_note="حيّك غير موجود في القائمة؟ نوصل إلى كل طنجة — راسلنا.",
 rules_t="مهم", rules=["Saha Express خدمة توصيل وليست صيدلية. يُشترى الدواء من صيدلية مرخّصة.","الوصفة الطبية ضرورية للأدوية التي تحتاج وصفة.","لا نقدّم نصائح طبية. في حالة الطوارئ اتصل بالرقم 15 أو 150."],
 faq_t="أسئلة شائعة", faq=[("كم ثمن التوصيل؟","يبدأ التوصيل من 20 درهم. الثمن النهائي حسب المسافة، ونؤكده لك على واتساب قبل الانطلاق."),("هل توصلون في الليل؟","نعم، نعمل 24/24 وكل أيام الأسبوع، حتى في الليل وأيام العطل، من صيدلية الحراسة المفتوحة."),("كيف أدفع؟","تدفع نقداً عند الاستلام: ثمن الدواء (بتذكرة الصيدلية) وثمن التوصيل."),("هل الوصفة ضرورية؟","نعم للأدوية التي تحتاج وصفة. للمنتجات الأخرى (شبه صيدلية، منتجات الأطفال…) أرسل الاسم فقط."),("أي أحياء؟","كل طنجة: مالاباطا، البرانص، إيبيريا، كاليفورنيا، النجمة، جبل الكبير، مسنانة، بني مكادة وكل الأحياء الأخرى.")],
 guide_t="صيدلية الحراسة في طنجة ليلاً: ماذا أفعل؟", guide_l="اقرأ الدليل",
 foot="Saha Express – التوصيل في طنجة", legal="خدمة توصيل. Saha Express ليست صيدلية ولا تبيع الأدوية."),
"en": dict(dir="ltr", path="en/", name="English",
 alt_night="Saha Express rider at night in Tangier near a pharmacy",
 open="Open 24/7", band_t="Need a medicine right now?", band_p="Send your prescription and we handle the rest. All of Tangier, day and night.",
 title="Night pharmacy delivery in Tangier 24/7 | Saha Express",
 desc="Saha Express picks up your medicine at the on-duty pharmacy and delivers it anywhere in Tangier, day and night. Send your prescription on WhatsApp. From 20 MAD.",
 kicker="Tangier · 24/7", h1="Your medicine delivered home, <span>even at night</span>",
 lead="Sick, with a child, or without a car? Send us your prescription on WhatsApp. We go to the open on-duty pharmacy and deliver to your door, anywhere in Tangier.",
 cta="Send my prescription", call="Call", price="Delivery from", dh="MAD",
 chips=["🌙 Day and night", "📍 All of Tangier", "📄 Prescription on WhatsApp", "💵 Pay on delivery"],
 how_t="How it works", how=[("📸","Send your prescription","Take a photo of the prescription (or type the product name) and send it on WhatsApp with your address."),("🏥","We go to the pharmacy","We find the open on-duty pharmacy and confirm the medicine price with you before buying."),("🛵","Delivered to your door","Our rider brings your order. You pay for the medicine and the delivery on arrival.")],
 form_t="Order now", f_name="Your first name", f_zone="Neighbourhood", f_addr="Address and landmark", f_note="Medicine or note (optional)",
 f_send="Send on WhatsApp", f_hint="WhatsApp opens with your message ready. Then add the photo of your prescription.",
 wa_hello="Hello Saha Express, I would like a pharmacy delivery.", wa_name="Name", wa_zone="Neighbourhood", wa_addr="Address", wa_note="Note", wa_photo="I will send you the photo of the prescription.",
 more_t="Not only pharmacy", more="We also deliver groceries, meals, documents and parcels anywhere in Tangier.",
 zones_t="We deliver in every neighbourhood of Tangier", zones_note="Your area is not listed? We still deliver everywhere in Tangier — message us.",
 rules_t="Important", rules=["Saha Express is a delivery service, not a pharmacy. Medicines are bought from a licensed pharmacy.","A prescription is required for prescription medicines.","We do not give medical advice. In an emergency, call 15 or 150."],
 faq_t="Frequently asked questions", faq=[("How much is delivery?","Delivery starts at 20 MAD. The exact price depends on distance; we confirm it on WhatsApp before leaving."),("Do you deliver at night?","Yes, we deliver 24/7, including nights and weekends, from the open on-duty pharmacy."),("How do I pay?","Cash on delivery: the medicine price (pharmacy receipt) plus delivery."),("Do I need a prescription?","Yes for prescription medicines. For other products (baby care, para-pharmacy…) just send the name."),("Which areas?","All of Tangier: Malabata, Branes, Iberia, Californie, Najma, Jbel Kbir, Mesnana, Beni Makada and every other area.")],
 guide_t="On-duty pharmacy in Tangier at night: what to do?", guide_l="Read the guide",
 foot="Saha Express – delivery in Tangier", legal="Delivery service. Saha Express is not a pharmacy and does not sell medicines."),
}
GUIDE = {
"fr": ["Il est 2 heures du matin, votre enfant a de la fièvre ou vous avez besoin d'un médicament, et toutes les pharmacies de votre quartier sont fermées. À Tanger, comme partout au Maroc, une pharmacie de garde reste ouverte chaque nuit, chaque week-end et chaque jour férié. Voici comment faire simplement.",
 ("Qu'est-ce qu'une pharmacie de garde ?","Les pharmacies de Tanger s'organisent par tour : chaque nuit et chaque jour férié, quelques pharmacies restent ouvertes pour toute la ville. La liste change tous les jours. Une pharmacie fermée affiche souvent sur sa porte l'adresse de la pharmacie de garde la plus proche."),
 ("Comment trouver la pharmacie de garde ?","Regardez l'affiche sur la porte d'une pharmacie fermée, demandez au gardien de nuit de votre quartier, ou contactez le Conseil régional de l'Ordre des pharmaciens. Les listes publiées en ligne ne sont pas toujours à jour : appelez avant de vous déplacer."),
 ("Et si vous ne pouvez pas vous déplacer ?","Avec Saha Express, vous n'avez pas besoin de chercher. Envoyez la photo de votre ordonnance sur WhatsApp : nous trouvons la pharmacie de garde ouverte, nous vous confirmons le prix, puis nous livrons chez vous, partout à Tanger, à partir de 20 DH."),
 ("Ce qu'il faut préparer","Une photo nette de l'ordonnance, votre adresse avec un repère (mosquée, café, école…), et l'argent liquide pour payer les médicaments et la livraison à la réception."),
 ("Urgence médicale","Une livraison ne remplace pas les secours. En cas d'urgence grave, appelez immédiatement le 15 (SAMU) ou le 150, ou rendez-vous aux urgences de l'hôpital le plus proche.")],
"ar": ["الساعة الثانية ليلاً، طفلك مريض أو تحتاج دواءً، وكل صيدليات الحي مغلقة. في طنجة، كما في كل المغرب، توجد كل ليلة وكل عطلة صيدلية حراسة مفتوحة. هذا ما يمكنك فعله ببساطة.",
 ("ما هي صيدلية الحراسة؟","تتناوب صيدليات طنجة: كل ليلة وكل يوم عطلة تبقى بعض الصيدليات مفتوحة لكل المدينة، والقائمة تتغير كل يوم. غالباً ما تضع الصيدلية المغلقة على بابها عنوان أقرب صيدلية حراسة."),
 ("كيف أجد صيدلية الحراسة؟","انظر إلى الورقة على باب صيدلية مغلقة، أو اسأل حارس الحي ليلاً، أو اتصل بالمجلس الجهوي لهيئة الصيادلة. القوائم المنشورة على الإنترنت ليست دائماً محدّثة، لذلك اتصل قبل أن تذهب."),
 ("وإذا لم تستطع الخروج؟","مع Saha Express لا تحتاج للبحث. أرسل صورة الوصفة على واتساب: نجد صيدلية الحراسة المفتوحة، نؤكد لك الثمن، ثم نوصل الدواء إلى بيتك في كل طنجة، ابتداءً من 20 درهم."),
 ("ماذا تحضّر؟","صورة واضحة للوصفة، وعنوانك مع علامة قريبة (مسجد، مقهى، مدرسة…)، والمال نقداً لدفع ثمن الدواء والتوصيل عند الاستلام."),
 ("حالة طارئة","التوصيل لا يعوّض الإسعاف. في حالة طارئة خطيرة اتصل فوراً بالرقم 15 أو 150، أو توجّه إلى مستعجلات أقرب مستشفى.")],
"en": ["It is 2 a.m., your child has a fever or you need a medicine, and every pharmacy in your area is closed. In Tangier, as everywhere in Morocco, an on-duty pharmacy stays open every night, weekend and public holiday. Here is what to do.",
 ("What is an on-duty pharmacy?","Tangier pharmacies take turns: every night and holiday a few pharmacies stay open for the whole city, and the list changes daily. A closed pharmacy usually shows the address of the nearest on-duty pharmacy on its door."),
 ("How to find it","Check the notice on the door of a closed pharmacy, ask your area's night guard, or contact the regional Council of Pharmacists. Lists published online are not always up to date, so call before you go."),
 ("If you can't go out","With Saha Express you don't need to search. Send a photo of your prescription on WhatsApp: we find the open on-duty pharmacy, confirm the price with you, and deliver to your door anywhere in Tangier, from 20 MAD."),
 ("What to prepare","A clear photo of the prescription, your address with a landmark (mosque, café, school…), and cash to pay for the medicine and delivery on arrival."),
 ("Medical emergency","Delivery does not replace emergency services. In a serious emergency, call 15 or 150 immediately or go to the nearest hospital emergency room.")],
}
SSLUG = "livraison-courses-repas-colis-tanger"
SERVICE = {
"fr": dict(t="Livraison de courses, repas, documents et colis à Tanger",
 d="Saha Express livre aussi vos courses, repas, documents et petits colis partout à Tanger, jour et nuit. Commande simple sur WhatsApp, à partir de 20 DH.",
 lead="La pharmacie n'est pas notre seul service. Vous avez oublié quelque chose au supermarché, vous voulez un repas d'un restaurant qui ne livre pas, ou vous devez envoyer un document à l'autre bout de Tanger ? Envoyez-nous un message : un livreur s'en occupe.",
 secs=[("Ce que nous livrons","Courses de l'épicerie ou du supermarché, repas de restaurants et snacks, documents et dossiers administratifs, clés, petits colis et cadeaux, produits bébé et para-pharmacie. Si cela tient dans notre caisse de livraison et que c'est légal, nous pouvons le transporter."),
       ("Comment commander","Écrivez sur WhatsApp ce que vous voulez et où il faut le prendre : le nom du magasin ou l'adresse, puis votre adresse avec un repère. Si nous devons acheter pour vous, nous vous confirmons le prix avant d'acheter. Vous payez à la réception, en espèces."),
       ("Prix et délais","La livraison commence à 20 DH dans Tanger. Le prix final dépend de la distance et nous vous l'annonçons avant de partir. La plupart des livraisons arrivent en moins d'une heure ; la nuit, comptez parfois un peu plus."),
       ("Quartiers desservis","Tout Tanger : Malabata, Branes, Iberia, Californie, Najma, Jbel Kbir, Marshan, Médina, Mesnana, Beni Makada, Casabarata, Boukhalef, Gzenaya et tous les autres quartiers.")]),
"ar": dict(t="توصيل المشتريات والوجبات والوثائق والطرود في طنجة",
 d="Saha Express توصل أيضاً مشترياتك ووجباتك ووثائقك وطرودك الصغيرة في كل طنجة، ليلاً ونهاراً. اطلب بسهولة على واتساب، ابتداءً من 20 درهم.",
 lead="الصيدلية ليست خدمتنا الوحيدة. نسيت شيئاً في السوق، أو تريد وجبة من مطعم لا يوصل، أو تحتاج إرسال وثيقة إلى الطرف الآخر من طنجة؟ أرسل لنا رسالة، وموزعنا يتكفل بالباقي.",
 secs=[("ماذا نوصل؟","مشتريات البقالة والسوق، وجبات المطاعم، الوثائق والملفات الإدارية، المفاتيح، الطرود الصغيرة والهدايا، منتجات الأطفال وشبه الصيدلية. إذا كان يدخل في صندوق التوصيل وكان قانونياً، يمكننا نقله."),
       ("كيف تطلب؟","اكتب على واتساب ما تريده ومن أين نأخذه: اسم المحل أو العنوان، ثم عنوانك مع علامة قريبة. إذا كان علينا الشراء لك، نؤكد لك الثمن قبل الشراء، وتدفع نقداً عند الاستلام."),
       ("الثمن والمدة","يبدأ التوصيل من 20 درهم داخل طنجة. الثمن النهائي حسب المسافة ونخبرك به قبل الانطلاق. أغلب الطلبات تصل في أقل من ساعة، وفي الليل قد تأخذ وقتاً أطول قليلاً."),
       ("الأحياء","كل طنجة: مالاباطا، البرانص، إيبيريا، كاليفورنيا، النجمة، جبل الكبير، مرشان، المدينة القديمة، مسنانة، بني مكادة، كاسابراطا، بوخالف، اكزناية وكل الأحياء الأخرى.")]),
"en": dict(t="Grocery, meal, document and parcel delivery in Tangier",
 d="Saha Express also delivers groceries, meals, documents and small parcels anywhere in Tangier, day and night. Easy ordering on WhatsApp, from 20 MAD.",
 lead="Pharmacy runs are not our only service. Forgot something at the supermarket, want a meal from a restaurant that doesn't deliver, or need a document taken across Tangier? Send us a message and a rider will handle it.",
 secs=[("What we deliver","Groceries, restaurant meals, documents and paperwork, keys, small parcels and gifts, baby care and para-pharmacy products. If it fits in our delivery box and it is legal, we can carry it."),
       ("How to order","Write on WhatsApp what you need and where to pick it up: the shop name or address, then your address with a landmark. If we need to buy for you, we confirm the price first. You pay cash on delivery."),
       ("Price and timing","Delivery starts at 20 MAD within Tangier. The final price depends on distance and we tell you before leaving. Most orders arrive in under an hour; at night it can take a little longer."),
       ("Areas we cover","All of Tangier: Malabata, Branes, Iberia, Californie, Najma, Jbel Kbir, Marshan, Medina, Mesnana, Beni Makada, Casabarata, Boukhalef, Gzenaya and every other area.")]),
}
NAV = {"fr": ("Accueil", "Pharmacie de garde la nuit", "Courses et colis"),
       "ar": ("الرئيسية", "صيدلية الحراسة ليلاً", "المشتريات والطرود"),
       "en": ("Home", "Night pharmacy guide", "Groceries and parcels")}

GSLUG = {"fr": "pharmacie-de-garde-tanger-nuit", "ar": "pharmacie-de-garde-tanger-nuit", "en": "pharmacie-de-garde-tanger-nuit"}

CSS = """:root{--bg:#f4f7fb;--card:#fff;--ink:#0b1b33;--muted:#5a6b82;--line:#e3e9f2;--navy:#0a2342;--navy2:#123a6b;--g:#12b886;--g2:#0ca678;--gl:#e7f8f1;--wa:#25d366;
--f:"Plus Jakarta Sans","Cairo",system-ui,sans-serif;color-scheme:light}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.7 var(--f)}
[dir=rtl] body{font-family:"Cairo","Plus Jakarta Sans",system-ui,sans-serif}
a{color:var(--g2)}.w{max-width:1120px;margin:0 auto;padding:0 16px}
header{position:sticky;top:0;z-index:20;background:#0a2342ee;backdrop-filter:blur(10px);color:#fff}
.nav{display:flex;align-items:center;justify-content:space-between;gap:12px;height:66px}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:21px;text-decoration:none;color:#fff}
.logo i{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,var(--g),#0b8f6a);display:grid;place-items:center;font-style:normal;box-shadow:0 6px 16px #12b88655}
.logo b{color:var(--g);margin-inline-start:4px}
.nav-r{display:flex;align-items:center;gap:10px}.langs{display:flex;gap:4px}
.langs a{font-size:12.5px;text-decoration:none;color:#c9d6ea;border-radius:99px;padding:4px 10px}.langs a.on{background:#ffffff1f;color:#fff}
.ncall{display:none;align-items:center;gap:6px;background:var(--g);color:#04281c;text-decoration:none;font-weight:800;border-radius:99px;padding:8px 16px;direction:ltr}
.heroW{background:radial-gradient(900px 500px at 85% -10%,#12b88633,transparent 60%),radial-gradient(700px 400px at -10% 110%,#2f6bd822,transparent 60%),linear-gradient(180deg,#0a2342,#0e2d55);color:#fff;margin:0 -16px;padding:0 16px;border-radius:0 0 36px 36px}
.hero{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:40px;align-items:center;padding:52px 0 64px}
.kicker{display:inline-flex;align-items:center;gap:8px;background:#ffffff14;border:1px solid #ffffff26;color:#d9fff0;font-weight:700;font-size:13px;border-radius:99px;padding:6px 14px}
.kicker i{width:8px;height:8px;border-radius:50%;background:var(--g);box-shadow:0 0 0 4px #12b88640;animation:p 1.6s infinite}
@keyframes p{50%{box-shadow:0 0 0 8px #12b88600}}
h1{font-size:clamp(34px,5.8vw,58px);line-height:1.12;margin:18px 0 14px;letter-spacing:-.02em;font-weight:800}
h1 span{background:linear-gradient(90deg,#5ef0bd,var(--g));-webkit-background-clip:text;background-clip:text;color:transparent}
[dir=rtl] h1{letter-spacing:0;line-height:1.35}
.lead{color:#c3d1e6;font-size:17.5px;max-width:52ch}
.acts{display:flex;flex-wrap:wrap;gap:12px;margin:26px 0 22px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:0;border-radius:16px;padding:16px 24px;font:800 16px/1 var(--f);text-decoration:none;cursor:pointer;transition:transform .15s}
.btn:hover{transform:translateY(-2px)}.btn.wa{background:var(--wa);color:#05391c;box-shadow:0 10px 26px #25d36655}.btn.ghost{background:#ffffff14;color:#fff;border:1px solid #ffffff33}
.btn svg{width:22px;height:22px}
.trust{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;max-width:520px}
.trust span{display:flex;align-items:center;gap:8px;font-size:14.5px;color:#e4ecf7}.trust span b{flex:none;display:grid;place-items:center;width:30px;height:30px;border-radius:9px;background:#ffffff14;font-size:15px}
.visual{position:relative}
.card3{background:#fff;color:var(--ink);border-radius:28px;padding:26px;box-shadow:0 30px 60px #0007}
.card3 .top{display:flex;align-items:center;justify-content:space-between}
.card3 .badge{background:var(--gl);color:var(--g2);font-weight:800;font-size:12.5px;border-radius:99px;padding:5px 12px}
.price{display:flex;align-items:baseline;gap:8px;margin:14px 0 4px}.price b{font-size:72px;line-height:1;font-weight:800;letter-spacing:-.03em}.price small{font-size:20px;font-weight:700;color:var(--muted)}
.card3 p{margin:0;color:var(--muted)}
.track{margin:18px 0 6px;display:grid;gap:12px}
.tr{display:flex;align-items:center;gap:12px}.tr i{flex:none;width:38px;height:38px;border-radius:12px;display:grid;place-items:center;font-style:normal;background:var(--bg)}
.tr.on i{background:var(--gl)}.tr span{font-weight:700;font-size:15px}
.card3 .tel{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px;background:var(--navy);border-radius:16px;padding:14px;color:#fff;text-decoration:none;font-weight:800;font-size:20px;direction:ltr}
.float2{position:absolute;inset-inline-start:-18px;bottom:-22px;background:#fff;color:var(--ink);border-radius:18px;padding:12px 16px;box-shadow:0 18px 40px #0005;display:flex;align-items:center;gap:10px;font-weight:700;font-size:14px}
.float2 b{font-size:22px}
section{padding:56px 0 8px}.eyebrow{color:var(--g2);font-weight:800;font-size:13px;letter-spacing:.12em;text-transform:uppercase}
h2{font-size:clamp(26px,4vw,38px);line-height:1.25;margin:6px 0 24px;letter-spacing:-.02em}
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;counter-reset:s}
.st{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:26px;position:relative;box-shadow:0 6px 20px #0a234210}
.st::before{counter-increment:s;content:counter(s);position:absolute;top:14px;inset-inline-end:22px;font-size:48px;font-weight:800;color:#0a234214}
.st b{display:grid;place-items:center;width:56px;height:56px;border-radius:18px;background:var(--gl);font-size:28px}
.st h3{margin:16px 0 6px;font-size:19px}.st p{margin:0;color:var(--muted);font-size:15px}
.order{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:24px;align-items:start}
form{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:26px;display:grid;gap:14px;box-shadow:0 10px 30px #0a234214}
label{display:grid;gap:6px;font-weight:700;font-size:14px}
input,select,textarea{font:inherit;color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:14px;padding:13px 14px;width:100%}
textarea{min-height:76px}input:focus,select:focus,textarea:focus{outline:0;border-color:var(--g)}
.hint{color:var(--muted);font-size:13px;margin:0}
.side{display:grid;gap:16px}.box{border-radius:24px;padding:24px}.box.safe{background:var(--navy);color:#e4ecf7}.box.safe b{color:#fff}
.box.more{background:var(--gl)}.box ul{margin:10px 0 0;padding-inline-start:20px}.box li{margin:7px 0}
.zones{display:flex;flex-wrap:wrap;gap:8px}.zones span{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:8px 14px;font-size:14.5px;font-weight:600}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px 20px;margin:10px 0}
summary{font-weight:800;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:10px}summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:22px;line-height:1;color:var(--g2)}details[open] summary::after{content:"–"}details p{margin:10px 0 0;color:var(--muted)}
.guide{display:flex;justify-content:space-between;align-items:center;gap:14px;background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:24px;padding:24px 26px;text-decoration:none;font-weight:800;font-size:18px}
.guide span:last-child{background:var(--g);color:#04281c;border-radius:99px;padding:8px 16px;font-size:14px;white-space:nowrap}
.cta-band{margin:56px 0 0;background:linear-gradient(135deg,var(--g),#0b8f6a);color:#fff;border-radius:28px;padding:34px 26px;text-align:center}
.cta-band h2{margin:0 0 6px;color:#fff}.cta-band p{margin:0 0 20px;color:#e9fff7}
article.post{max-width:740px;margin:0 auto;padding:40px 0}article.post h1{color:var(--ink);font-size:clamp(28px,5vw,42px)}article.post .lead{color:var(--muted)}
article.post h2{font-size:22px;margin:30px 0 8px}
footer{background:var(--navy);color:#b9c7dc;padding:34px 0 110px;font-size:14px;text-align:center;margin-top:60px}footer b{color:#fff;font-size:17px}footer a{color:#5ef0bd}
.float{position:fixed;bottom:18px;inset-inline-end:18px;width:62px;height:62px;border-radius:50%;background:var(--wa);display:grid;place-items:center;box-shadow:0 10px 26px #0006;z-index:30}
.float svg{width:32px;height:32px}
@media (min-width:761px){.ncall{display:inline-flex}}
@media (max-width:760px){.hero,.order{grid-template-columns:1fr}.steps{grid-template-columns:1fr}.hero{padding:30px 0 56px;gap:30px}.float2{inset-inline-start:10px}
.guide{flex-direction:column;align-items:flex-start}.langs a{padding:4px 7px}.btn{width:100%}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}

.hero-img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;object-position:center 60%;border-radius:28px;box-shadow:0 30px 60px #0008}
.visual .card3{position:absolute;inset-inline-start:-24px;bottom:-26px;width:min(270px,80%);padding:18px 20px}
.visual .card3 .price b{font-size:54px}.visual .card3 .tel{font-size:17px;padding:11px;margin-top:12px}
.st{padding:0;overflow:hidden;display:flex;flex-direction:column}.st img{display:block;width:100%;height:220px;object-fit:cover}
.st-ic{height:220px;display:grid;place-items:center;font-size:84px;background:linear-gradient(135deg,var(--gl),#d5f3e7)}
.st-b{padding:20px 22px 24px}.st::before{z-index:2;color:#ffffffcc;text-shadow:0 2px 10px #0006;top:10px}
@media (max-width:760px){.hero-img{aspect-ratio:4/4.4;object-position:center 55%}.visual .card3{position:relative;inset:auto;width:auto;margin:-60px 14px 0}.hero{padding-bottom:40px}}

.fnav{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 18px;margin-bottom:14px}.fnav a{color:#cfe0f5;text-decoration:none;font-weight:600}
"""
WAICON = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.4 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.4-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.8s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.4.5-.3.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg>'

def page(lang, rel, title, desc, body, schema):
    L = T[lang]; up = "../" * rel.count("/")
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{URL}/{T[l]["path"]}{rel}">' for l in T) + f'<link rel="alternate" hreflang="x-default" href="{URL}/{rel}">'
    root = "../" * (L["path"] + rel).count("/") or "./"
    langs = "".join(f'<a href="{root}{T[l]["path"]}{rel}" class="{"on" if l==lang else ""}" hreflang="{l}">{T[l]["name"]}</a>' for l in T)
    home = f'{root}{L["path"]}'
    return f"""<!doctype html><html lang="{lang}" dir="{L['dir']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{URL}/{L['path']}{rel}">{alts}
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="{URL}/img/night.webp"><meta name="theme-color" content="#0f8a5f">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛵</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"><style>{CSS}</style><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head><body>
<header><div class="w nav"><a class="logo" href="{home}"><i>🛵</i><span>Saha<b>Express</b></span></a><div class="nav-r"><nav class="langs">{langs}</nav><a class="ncall" href="tel:{TEL}">📞 {TEL_SHOW}</a></div></div></header>
<main class="w">{body}</main>
<footer><div class="w"><nav class="fnav"><a href="{root}{L['path']}">{e(NAV[lang][0])}</a><a href="{root}{L['path']}{GSLUG[lang]}/">{e(NAV[lang][1])}</a><a href="{root}{L['path']}{SSLUG}/">{e(NAV[lang][2])}</a></nav><b>{e(L['foot'])}</b><br>WhatsApp / Tel: <a href="tel:{TEL}" dir="ltr">{TEL_SHOW}</a><br>{e(L['legal'])}<br>© Saha Express</div></footer>
<a class="float" href="https://wa.me/{WA}?text={quote(L['wa_hello'] + SRC)}" aria-label="WhatsApp">{WAICON}</a></body></html>"""

def business(lang):
    L = T[lang]
    return {"@context":"https://schema.org","@type":"LocalBusiness","name":"Saha Express","description":L["desc"],"url":f"{URL}/{L['path']}","telephone":TEL,
            "areaServed":[{"@type":"City","name":"Tanger"}] + [{"@type":"Place","name":z + ", Tanger"} for z in ZONES[:12]],
            "geo":{"@type":"GeoCoordinates","latitude":35.7595,"longitude":-5.834},"image":f"{URL}/img/night.webp",
            "knowsLanguage":["fr","ar","en"],"currenciesAccepted":"MAD","paymentAccepted":"Cash","address":{"@type":"PostalAddress","addressLocality":"Tanger","addressCountry":"MA"},
            "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"},
            "priceRange":"20+ MAD"}

def home(lang):
    L = T[lang]
    IMG = "../img/" if L["path"] else "img/"
    opts = "".join(f"<option>{e(z)}</option>" for z in ZONES)
    body = f"""
<div class="heroW"><div class="hero"><div><span class="kicker"><i></i>{e(L['kicker'])}</span><h1>{L['h1']}</h1><p class="lead">{e(L['lead'])}</p>
<div class="acts"><a class="btn wa" href="https://wa.me/{WA}?text={quote(L['wa_hello'] + SRC)}">{WAICON.replace('#fff','#05391c')} {e(L['cta'])}</a><a class="btn ghost" href="tel:{TEL}">📞 {e(L['call'])}</a></div>
<div class="trust">{''.join(f'<span><b>{c.split(" ",1)[0]}</b>{e(c.split(" ",1)[1])}</span>' for c in L['chips'])}</div></div>
<div class="visual"><img class="hero-img" src="{IMG}night.webp" width="760" height="1352" alt="{e(L['alt_night'])}" fetchpriority="high">
<div class="card3"><div class="top"><span class="badge">● {e(L['open'])}</span></div>
<div class="price"><b>20</b><small>{e(L['dh'])}</small></div><p>{e(L['price'])} · {e(L['chips'][1].split(" ",1)[1])}</p>
<a class="tel" href="tel:{TEL}">📞 {TEL_SHOW}</a></div></div></div></div>
<section><div class="eyebrow">{e(L['kicker'].split('·')[0].strip())}</div><h2>{e(L['how_t'])}</h2><div class="steps">{''.join(f'<div class="st">' + (f'<img src="{IMG}{im}.webp" width="640" height="{ih}" alt="{e(a)}" loading="lazy">' if im else f'<div class="st-ic">{i}</div>') + f'<div class="st-b"><h3>{e(a)}</h3><p>{e(b)}</p></div></div>' for (i,a,b),(im,ih) in zip(L['how'],[("prescription",1138),("pharmacy",760),("door",960)]))}</div></section>
<section id="order"><h2>{e(L['form_t'])}</h2><div class="order">
<form id="f"><label>{e(L['f_name'])}<input name="n" required maxlength="60"></label>
<label>{e(L['f_zone'])}<select name="z">{opts}<option>…</option></select></label>
<label>{e(L['f_addr'])}<input name="a" required maxlength="160"></label>
<label>{e(L['f_note'])}<textarea name="m" maxlength="400"></textarea></label>
<button class="btn wa" type="submit">{WAICON.replace('#fff','#063d1f').replace('<svg','<svg style="width:20px;height:20px"')} {e(L['f_send'])}</button><p class="hint">{e(L['f_hint'])}</p></form>
<div class="side"><div class="box safe"><b>🛡️ {e(L['rules_t'])}</b><ul>{''.join(f'<li>{e(r)}</li>' for r in L['rules'])}</ul></div><div class="box more"><b>📦 {e(L['more_t'])}</b><p style="margin:6px 0 0">{e(L['more'])}</p></div></div></div></section>
<section><h2>{e(L['zones_t'])}</h2><div class="zones">{''.join(f'<span>📍 {e(z)}</span>' for z in ZONES)}</div><p class="hint" style="margin-top:12px">{e(L['zones_note'])}</p></section>
<section class="faq"><h2>{e(L['faq_t'])}</h2>{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in L['faq'])}</section>
<section style="display:grid;gap:14px"><a class="guide" href="{GSLUG[lang]}/"><span>📖 {e(L['guide_t'])}</span><span>{e(L['guide_l'])} →</span></a><a class="guide" href="{SSLUG}/"><span>📦 {e(SERVICE[lang]['t'])}</span><span>{e(L['guide_l'])} →</span></a></section>
<div class="cta-band"><h2>{e(L['band_t'])}</h2><p>{e(L['band_p'])}</p><a class="btn wa" style="background:#fff" href="https://wa.me/{WA}?text={quote(L['wa_hello'] + SRC)}">{WAICON.replace('#fff','#0b8f6a')} {e(L['cta'])}</a></div>
<script>
var f=document.getElementById('f'),L={json.dumps({k:L[k] for k in ('wa_hello','wa_name','wa_zone','wa_addr','wa_note','wa_photo')},ensure_ascii=False)};
f.onsubmit=function(ev){{ev.preventDefault();var t=L.wa_hello+'\\n'+L.wa_name+': '+f.n.value+'\\n'+L.wa_zone+': '+f.z.value+'\\n'+L.wa_addr+': '+f.a.value+(f.m.value?'\\n'+L.wa_note+': '+f.m.value:'')+'\\n'+L.wa_photo+{json.dumps(SRC)};
window.open('https://wa.me/{WA}?text='+encodeURIComponent(t),'_blank');}};
</script>"""
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in L['faq']]}
    return page(lang, "", L["title"], L["desc"], body, [business(lang), faq])

def guide(lang):
    L, G = T[lang], GUIDE[lang]
    body = f'<article class="post"><h1>{e(L["guide_t"])}</h1><p class="lead">{e(G[0])}</p>' + "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h,p in G[1:]) + \
           f'<p><a class="btn wa" href="https://wa.me/{WA}?text={quote(L["wa_hello"] + SRC)}">📄 {e(L["cta"])}</a></p></article>'
    sch = {"@context":"https://schema.org","@type":"Article","headline":L["guide_t"],"inLanguage":lang,"publisher":{"@type":"Organization","name":"Saha Express"}}
    return page(lang, GSLUG[lang] + "/", L["guide_t"] + " | Saha Express", G[0][:155], body, sch)

def service(lang):
    L, S = T[lang], SERVICE[lang]
    body = f'<article class="post"><h1>{e(S["t"])}</h1><p class="lead">{e(S["lead"])}</p>' + "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in S["secs"]) + \
           f'<p><a class="btn wa" href="https://wa.me/{WA}?text={quote(S["t"] + " – " + L["wa_hello"].split(",")[0] + SRC)}">💬 WhatsApp</a></p></article>'
    sch = {"@context": "https://schema.org", "@type": "Service", "name": S["t"], "serviceType": "Delivery", "inLanguage": lang,
           "areaServed": {"@type": "City", "name": "Tanger"}, "provider": {"@type": "LocalBusiness", "name": "Saha Express", "telephone": TEL, "url": URL + "/"}}
    return page(lang, SSLUG + "/", S["t"] + " | Saha Express", S["d"], body, sch)

if OUT.exists(): shutil.rmtree(OUT)
urls = []
for lang, L in T.items():
    d = OUT / L["path"]; d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(home(lang), encoding="utf-8"); urls.append(f"{URL}/{L['path']}")
    g = d / GSLUG[lang]; g.mkdir(parents=True, exist_ok=True)
    (g / "index.html").write_text(guide(lang), encoding="utf-8"); urls.append(f"{URL}/{L['path']}{GSLUG[lang]}/")
    sv = d / SSLUG; sv.mkdir(parents=True, exist_ok=True)
    (sv / "index.html").write_text(service(lang), encoding="utf-8"); urls.append(f"{URL}/{L['path']}{SSLUG}/")
shutil.copytree(Path(__file__).parent / "img", OUT / "img")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n")
import datetime as _dt
_today = _dt.date.today().isoformat()
def _alts(u):
    rel = u.replace(URL + "/", "")
    for l in T:
        if T[l]["path"] and rel.startswith(T[l]["path"]):
            rel = rel[len(T[l]["path"]):]
    return "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{URL}/{T[l]["path"]}{rel}"/>' for l in T)
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">' +
    "".join(f"<url><loc>{u}</loc><lastmod>{_today}</lastmod>{_alts(u)}</url>" for u in urls) + "</urlset>")
(OUT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY)
(OUT / "CNAME").write_text("www.sahaexpresstanger.com\n")
(OUT / ".nojekyll").write_text("")
(OUT / "google1a66cd67b82a0599.html").write_text("google-site-verification: google1a66cd67b82a0599.html")
print("built", len(urls), "pages")
