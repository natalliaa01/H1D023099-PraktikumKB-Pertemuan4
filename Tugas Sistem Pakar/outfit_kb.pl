% outfit_kb.pl - Prolog Knowledge Base for Outfit Recommendation System

% Define clothing items by category, occasion, and weather
% Format: item_options(Category, Occasion, Weather, ItemList).

% Tops options
item_options(tops, formal, hot, ['Kemeja katun lengan pendek', 'Kemeja linen tipis', 'Blus sutra']).
item_options(tops, formal, warm, ['Kemeja formal lengan panjang', 'Blus semi-formal', 'Kemeja katun lengan 3/4']).
item_options(tops, formal, cold, ['Kemeja tebal', 'Sweater kasmir', 'Turtle neck']).
item_options(tops, formal, rainy, ['Kemeja lengan panjang', 'Blus dengan lapisan dalam']).

item_options(tops, casual, hot, ['Kaos katun', 'Tank top', 'Crop top', 'T-shirt vintage']).
item_options(tops, casual, warm, ['Kaos lengan panjang', 'Henley shirt', 'Polo shirt']).
item_options(tops, casual, cold, ['Sweater rajut', 'Hoodie', 'Sweatshirt']).
item_options(tops, casual, rainy, ['Kaos lengan panjang', 'Sweater tipis']).

item_options(tops, sports, hot, ['Singlet olahraga', 'Sport bra', 'Kaos dry-fit']).
item_options(tops, sports, warm, ['Kaos olahraga lengan panjang', 'Jersey ringan']).
item_options(tops, sports, cold, ['Jaket olahraga', 'Sweater training', 'Base layer thermal']).
item_options(tops, sports, rainy, ['Kaos olahraga waterproof', 'Jaket lari ringan']).

% Bottoms options
item_options(bottoms, formal, hot, ['Celana bahan tipis', 'Rok A-line', 'Celana kulot']).
item_options(bottoms, formal, warm, ['Celana bahan', 'Rok pensil', 'Celana ankle-length']).
item_options(bottoms, formal, cold, ['Celana wool', 'Rok panjang', 'Celana bahan tebal']).
item_options(bottoms, formal, rainy, ['Celana bahan anti air', 'Rok panjang']).

item_options(bottoms, casual, hot, ['Celana pendek', 'Rok mini', 'Jeans pendek', 'Rok flare']).
item_options(bottoms, casual, warm, ['Jeans', 'Celana chino', 'Rok midi']).
item_options(bottoms, casual, cold, ['Jeans tebal', 'Celana cargo', 'Legging']).
item_options(bottoms, casual, rainy, ['Jeans', 'Celana panjang waterproof']).

item_options(bottoms, sports, hot, ['Celana pendek olahraga', 'Legging pendek', 'Rok tennis']).
item_options(bottoms, sports, warm, ['Celana training', 'Legging 3/4', 'Jogger pants']).
item_options(bottoms, sports, cold, ['Celana training tebal', 'Legging thermal', 'Sweatpants']).
item_options(bottoms, sports, rainy, ['Celana training waterproof', 'Legging tahan air']).

% Outerwear options
item_options(outerwear, formal, hot, ['Tidak diperlukan', 'Blazer ultra tipis (opsional)']).
item_options(outerwear, formal, warm, ['Blazer ringan', 'Cardigan formal', 'Jas tipis']).
item_options(outerwear, formal, cold, ['Blazer wol', 'Coat formal', 'Trench coat']).
item_options(outerwear, formal, rainy, ['Blazer waterproof', 'Trench coat', 'Jas hujan formal']).

item_options(outerwear, casual, hot, ['Tidak diperlukan']).
item_options(outerwear, casual, warm, ['Cardigan tipis', 'Jaket denim', 'Kemeja flannel']).
item_options(outerwear, casual, cold, ['Jaket tebal', 'Parka', 'Coat casual', 'Puffer jacket']).
item_options(outerwear, casual, rainy, ['Jaket hujan', 'Windbreaker', 'Parka tahan air']).

item_options(outerwear, sports, hot, ['Tidak diperlukan']).
item_options(outerwear, sports, warm, ['Jaket olahraga ringan', 'Windbreaker tipis']).
item_options(outerwear, sports, cold, ['Jaket olahraga tebal', 'Windbreaker berlapis', 'Down jacket']).
item_options(outerwear, sports, rainy, ['Jaket hujan olahraga', 'Anorak', 'Poncho olahraga']).

% Shoes options
item_options(shoes, formal, hot, ['Loafer', 'Flat shoes', 'Sepatu pantofel']).
item_options(shoes, formal, warm, ['Oxford shoes', 'Sepatu kulit', 'Heels']).
item_options(shoes, formal, cold, ['Boots formal', 'Chelsea boots', 'Sepatu kulit berlapis']).
item_options(shoes, formal, rainy, ['Boots tahan air', 'Sepatu kulit waterproof']).

item_options(shoes, casual, hot, ['Sandal', 'Slip-on', 'Sneakers ringan', 'Espadrilles']).
item_options(shoes, casual, warm, ['Sneakers', 'Sepatu kanvas', 'Moccasin']).
item_options(shoes, casual, cold, ['Boots casual', 'Sneakers tebal', 'High-top sneakers']).
item_options(shoes, casual, rainy, ['Boots hujan', 'Sneakers waterproof']).

item_options(shoes, sports, hot, ['Sepatu lari ringan', 'Training shoes', 'Sandal olahraga']).
item_options(shoes, sports, warm, ['Sepatu olahraga', 'Cross-trainer', 'Athletic shoes']).
item_options(shoes, sports, cold, ['Sepatu trail', 'Sneakers olahraga tebal', 'Hiking shoes']).
item_options(shoes, sports, rainy, ['Trail shoes waterproof', 'Sepatu olahraga tahan air']).

% Accessories options
item_options(accessories, formal, hot, ['Kacamata hitam', 'Tas kerja', 'Jam tangan', 'Scarf tipis']).
item_options(accessories, formal, warm, ['Jam tangan', 'Dasi', 'Tas kerja', 'Belt kulit']).
item_options(accessories, formal, cold, ['Syal wol', 'Sarung tangan kulit', 'Tas kerja', 'Topi formal']).
item_options(accessories, formal, rainy, ['Payung', 'Tas waterproof', 'Syal anti air']).

item_options(accessories, casual, hot, ['Topi bucket', 'Kacamata hitam', 'Tas selempang', 'Gelang']).
item_options(accessories, casual, warm, ['Topi baseball', 'Sling bag', 'Jam tangan casual']).
item_options(accessories, casual, cold, ['Beanie', 'Syal rajut', 'Sarung tangan', 'Backpack']).
item_options(accessories, casual, rainy, ['Payung pocket', 'Tas anti air', 'Topi hujan']).

item_options(accessories, sports, hot, ['Sport cap', 'Wristband', 'Tas olahraga', 'Headband']).
item_options(accessories, sports, warm, ['Beanie sport', 'Gym bag', 'Smart watch', 'Bottle holder']).
item_options(accessories, sports, cold, ['Ear warmer', 'Sarung tangan olahraga', 'Syal microfiber']).
item_options(accessories, sports, rainy, ['Tas waterproof', 'Penutup sepatu', 'Payung mini']).

% Rules for filtering based on gender preference
filter_by_gender(ItemList, masculine, FilteredList) :-
    exclude(is_feminine_item, ItemList, FilteredList).

filter_by_gender(ItemList, feminine, FilteredList) :-
    ItemList = FilteredList.  % No filtering needed for feminine preference

filter_by_gender(ItemList, neutral, FilteredList) :-
    ItemList = FilteredList.  % No filtering needed for neutral preference

% Helper predicates to identify feminine items
is_feminine_item(Item) :-
    feminine_keywords(Keywords),
    member(Keyword, Keywords),
    sub_atom(Item, _, _, _, Keyword).

feminine_keywords(['Blus', 'Rok', 'Dress', 'Crop top']).

% Rules for filtering based on modest preference
filter_by_modesty(ItemList, modest, FilteredList) :-
    exclude(is_immodest_item, ItemList, FilteredList).

filter_by_modesty(ItemList, none, FilteredList) :-
    ItemList = FilteredList.  % No filtering needed for no modesty preference

% Helper predicates to identify immodest items
is_immodest_item(Item) :-
    immodest_keywords(Keywords),
    member(Keyword, Keywords),
    sub_atom(Item, _, _, _, Keyword).

immodest_keywords(['Crop top', 'Tank top', 'Singlet', 'Rok mini', 'Celana pendek']).

% Season determination based on month
season(Month, spring) :- Month >= 3, Month =< 5.
season(Month, summer) :- Month >= 6, Month =< 8.
season(Month, fall) :- Month >= 9, Month =< 11.
season(Month, winter) :- Month =< 2; Month = 12.

% Color recommendations based on season
color_recommendation(spring, 'Warna-warna pastel seperti mint, peach, atau baby blue cocok untuk musim semi.').
color_recommendation(summer, 'Warna-warna cerah seperti kuning, biru laut, atau coral ideal untuk musim panas.').
color_recommendation(fall, 'Warna-warna hangat seperti maroon, olive, atau mustard cocok untuk musim gugur.').
color_recommendation(winter, 'Warna-warna gelap seperti navy, burgundy, atau forest green ideal untuk musim dingin.').

% Weather tips
weather_tip(hot, '☀️ Tip: Pilih bahan yang breathable dan menyerap keringat. Jangan lupa sunscreen!').
weather_tip(rainy, '🌧️ Tip: Bawa payung atau jas hujan dan hindari sepatu berbahan suede atau kulit yang mudah rusak terkena air.').
weather_tip(cold, '❄️ Tip: Gunakan teknik layering untuk menjaga tubuh tetap hangat. Inner thermal bisa jadi pilihan tepat.').
weather_tip(warm, '🌤️ Tip: Pilih lapisan yang bisa ditambah atau dikurangi sesuai dengan perubahan suhu sepanjang hari.').

% Occasion tips
occasion_tip(formal, '💼 Tip: Pilih aksesoris minimalis namun elegan untuk tampilan profesional.').
occasion_tip(casual, '🛍️ Tip: Prioritaskan kenyamanan namun tetap stylish dengan memadukan item basic dan statement piece.').
occasion_tip(sports, '🏃 Tip: Utamakan kenyamanan dan mobilitas. Bawa botol air dan handuk kecil.').

% Complete outfit recommendation
recommend_outfit(Occasion, Weather, Gender, Modesty, Month, RecommendationText) :-
    % Get items for each category
    item_options(tops, Occasion, Weather, TopOptions),
    item_options(bottoms, Occasion, Weather, BottomOptions),
    item_options(outerwear, Occasion, Weather, OuterwearOptions),
    item_options(shoes, Occasion, Weather, ShoeOptions),
    item_options(accessories, Occasion, Weather, AccessoryOptions),
    
    % Apply filters based on gender and modesty preferences
    filter_by_gender(TopOptions, Gender, GenderFilteredTops),
    filter_by_gender(BottomOptions, Gender, GenderFilteredBottoms),
    
    filter_by_modesty(GenderFilteredTops, Modesty, FilteredTops),
    filter_by_modesty(GenderFilteredBottoms, Modesty, FilteredBottoms),
    
    % Get season and associated color recommendation
    season(Month, Season),
    color_recommendation(Season, ColorRec),
    
    % Get tips
    weather_tip(Weather, WeatherTip),
    occasion_tip(Occasion, OccasionTip),
    
    % Construct recommendation text
    format(atom(RecommendationText), 
           '=== REKOMENDASI OUTFIT ===\n\n👕 Atasan: %w\n\n👖 Bawahan: %w\n\n🧥 Outer: %w\n\n👟 Alas Kaki: %w\n\n👜 Aksesoris: %w\n\n🎨 %w\n\n%w\n\n%w',
           [FilteredTops, FilteredBottoms, OuterwearOptions, ShoeOptions, AccessoryOptions, ColorRec, WeatherTip, OccasionTip]).