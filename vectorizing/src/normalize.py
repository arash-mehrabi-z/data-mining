class Normal():
    normal_dict = {
        'آ' : '[ﺁﺂ]',
        'ا' : '[ﺍﺎٲٵﭐﭑﺃﺄٳﺇﺈإأꙇ]',
        'ب' : '[ٮٻڀݐݒݔݕݖﭒﭓﭔﭕﺏﺐﺑﺒ]',
        'پ' : '[ﭖﭗﭘﭙﭚﭛﭜﭝ]',
        'ت' : '[ٹٺټٿݓﭞﭟﭠﭡﭦﭧﭨﭩﺕﺖﺗﺘ]',
        'ث' : '[ٽݑﺙﺚﺛﺜﭢﭣﭤﭥ]',
        'ج' : '[ڃڄﭲﭳﭴﭵﭶﭷﭸﭹﺝﺞﺟﺠ]',
        'چ' : '[ڇڿﭺﭻݘﭼﭽﭾﭿﮀﮁݯ]',
        'ح' : '[ځڂڅݗݮﺡﺢﺣﺤ]',
        'خ' : '[ﺥﺦﺧﺨ]',
        'د' : '[ڈډڊڋڍۮݙݚﮂﮃﮄﮈﮉﺩﺪ]',
        'ذ' : '[ڌﺫﺬڎڏڐﮅﮆﮇ]',
        'ر' : '[ڑڒړڔڕږۯݛﮌﮍﺭﺮ]',
        'ز' : '[ڗݫݬﺯﺰ]',
        'ژ' : '[ڙﮊﮋ]',
        'س' : '[ښڛﺱﺲﺳﺴ]',
        'ش' : '[ڜۺﺵﺶﺷﺸݜݭ]',
        'ص' : '[ڝڞﺹﺺﺻﺼ]',
        'ض' : '[ۻﺽﺾﺿﻀ]',
        'ط' : '[ﻁﻂﻃﻄ]',
        'ظ' : '[ﻅﻆﻇﻈڟ]',
        'ع' : '[ڠݝݞݟﻉﻊﻋﻌ]',
        'غ' : '[ۼﻍﻎﻏﻐ]',
        'ف' : '[ڡڢڣڤڥڦݠݡﭪﭫﭬﭭﭮﭯﭰﭱﻑﻒﻓﻔᓅ]',
        'ق' : '[ٯڧڨﻕﻖﻗﻘ]',
        'ک' : '[كػؼڪګڬڭڮݢݣݤﮎﮏﮐﮑﯓﯔﯕﯖﻙﻚﻛﻜ]',
        'گ' : '[ڰڱڲڳڴﮒﮓﮔﮕﮖﮗﮘﮙﮚﮛﮜﮝ]',
        'ل' : '[ڵڶڷڸݪﻝﻞﻟﻠ]',
        'م' : '[۾ݥݦﻡﻢﻣﻤ]',
        'ن' : '[ڹںڻڼڽݧݨݩﮞﮟﮠﮡﮢﮣﻥﻦﻧﻨ]',
        'و' : '[ٶٷﯗﯘﯙﯚﯛﯜﯝﯞﯟﺅﺆۄۅۆۇۈۉۊۋۏﯠﯡﯢﯣﻭﻮؤפ]',
        'ه' : '[ھۿۀہۂۃەﮤﮥﮦﮧﮨﮩﮪﮫﮬﮭﺓﺔﻩﻪﻫﻬة]',
        'ی' : '[ؠؽؾؿىيٸۍێېۑےۓﮮﮯﮰﮱﯤﯥﯦﯧﯼﯽﯾﯿﻯﻰﻱﻲﻳﻴﯨﯩۦﺉﺊﺋﺌئ]',
        '۰' : '[٠𝟢𝟬]',
        '۱' : '[١𝟣𝟭⑴⒈⓵①❶𝟙𝟷ı]',
        '۲' : '[٢𝟤𝟮⑵⒉⓶②❷²𝟐𝟸𝟚ᒿշ]',
        '۳' : '[٣𝟥𝟯⑶⒊⓷③❸³ვ]',
        '۴' : '[٤𝟦𝟰⑷⒋⓸④❹⁴]',
        '۵' : '[٥𝟧𝟱⑸⒌⓹⑤❺⁵]',
        '۶' : '[٦𝟨𝟲⑹⒍⓺⑥❻⁶]',
        '۷' : '[٧𝟩𝟳⑺⒎⓻⑦❼⁷]',
        '۸' : '[٨𝟪𝟴⑻⒏⓼⑧❽⁸]',
        '۹' : '[٩𝟫𝟵⑼⒐⓽⑨❾⁹]',
    }