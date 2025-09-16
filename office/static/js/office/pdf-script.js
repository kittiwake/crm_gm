// playground requires you to assign document definition to a variable called dd

function sumToString(_number){
    var _arr_numbers = new Array();
    _arr_numbers[1] = new Array('', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать');
    _arr_numbers[2] = new Array('', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто');
    _arr_numbers[3] = new Array('', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот');
    function number_parser(_num, _desc) {
        var _string = '';
        var _num_hundred = '';
        if (_num.length == 3) {
            _num_hundred = _num.substr(0, 1);
            _num = _num.substr(1, 3);
            _string = _arr_numbers[3][_num_hundred] + ' ';
        }
        if (_num < 20) _string += _arr_numbers[1][parseFloat(_num)] + ' ';
        else {
            var _first_num = _num.substr(0, 1);
            var _second_num = _num.substr(1, 2);
            _string += _arr_numbers[2][_first_num] + ' ' + _arr_numbers[1][_second_num] + ' ';
        }
        switch (_desc){
            //case 0:
            //    var _last_num = parseFloat(_num.substr(-1));
            //    if (_last_num == 1) _string += 'рубль';
            //    else if (_last_num > 1 && _last_num < 5) _string += 'рубля';
            //    else _string += 'рублей';
            //    break;
            case 1:
                var _last_num = parseFloat(_num.substr(-1));
                if (_last_num == 1) _string += 'тысяча ';
                else if (_last_num > 1 && _last_num < 5) _string += 'тысячи ';
                else _string += 'тысяч ';
                _string = _string.replace('один ', 'одна ');
                _string = _string.replace('два ', 'две ');
                break;
            case 2:
                var _last_num = parseFloat(_num.substr(-1));
                if (_last_num == 1) _string += 'миллион ';
                else if (_last_num > 1 && _last_num < 5) _string += 'миллиона ';
                else _string += 'миллионов ';
                break;
            case 3:
                var _last_num = parseFloat(_num.substr(-1));
                if (_last_num == 1) _string += 'миллиард ';
                else if (_last_num > 1 && _last_num < 5) _string += 'миллиарда ';
                else _string += 'миллиардов ';
                break;
        }
        _string = _string.replace('  ', ' ');
        return _string;
    }
    function decimals_parser(_num) {
        var _first_num = _num.substr(0, 1);
        var _second_num = parseFloat(_num.substr(1, 2));
        var _string = ' ' + _first_num + _second_num;
        if (_second_num == 1) _string += ' копейка';
        else if (_second_num > 1 && _second_num < 5) _string += ' копейки';
        else _string += ' копеек';
        return _string;
    }
    if (!_number || _number == 0) return false;
    if (typeof _number !== 'number') {
        _number = _number.replace(',', '.');
        _number = parseFloat(_number);
        if (isNaN(_number)) return false;
    }
    _number = _number.toFixed(2);
    if(_number.indexOf('.') != -1) {
        var _number_arr = _number.split('.');
        var _number = _number_arr[0];
        var _number_decimals = _number_arr[1];
    }
    var _number_length = _number.length;
    var _string = '';
    var _num_parser = '';
    var _count = 0;
    for (var _p = (_number_length - 1); _p >= 0; _p--) {
        var _num_digit = _number.substr(_p, 1);
        _num_parser = _num_digit +  _num_parser;
        if ((_num_parser.length == 3 || _p == 0) && !isNaN(parseFloat(_num_parser))) {
            _string = number_parser(_num_parser, _count) + _string;
            _num_parser = '';
            _count++;
        }
    }
    //if (_number_decimals) _string += decimals_parser(_number_decimals);
    return _string;
}

function delitel(str,pos){
    if(str.length > pos){
        //берем pos символа
        var nach = str.substr(0,pos);
        // от конца ищем пробел
        var ps = nach.lastIndexOf(' ');
        //берем подстроку до этого пробела
        var strpart1 = str.substr(0, ps);
        //из начальной строки отбрасываем подстроку
        var last = str.substr(ps+1);
        var razdel = strpart1 + '&' + last;
        return (razdel);
    }
}

function prihKass() {

    var cont = document.getElementById('zakaz').innerText;
    //дату не сегодня, а дату плановую
    var ooo, company,uraddr,bank;
    ooo = document.getElementById('ooo').value;
    
switch (ooo) {
  case 'gm':
    company = 'ООО «Галерея мебели»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 2';
    bank = 'ИНН/КПП 5012061688/504001001 р/с 40702810240040019106 в ПАО СБЕРБАНК г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистов Д.А.';
    break;
  case 'als':
    company = 'ООО «Александрия»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 3';
    bank = 'ИНН/КПП 5041202326/504001001 ОГРН 1155012001671 ОКТМО 47664000 р/с 40702810140000007326 в ПАО "Сбербанк России" г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистова Н.П.';
    break;
  case 'mk':
    company = ' ИП БАРЛАДЯН ЕВГЕНИЙ ВАСИЛЬЕВИЧ';
    uraddr = '141851 Дмитровский р-н дер. Голявино д.35';
    bank = 'ИНН 502480559844\nОГРНИП 313500734000015 ОКТМО 46608101166 р/с 40802810802640002367 в АО "АЛЬФА-БАНК" г.Москва БИК 044525593 \nк/с 30101810200000000593';
    glbuh = 'Барладян Е.В.';
    break;
  default:
    company = 'ООО «Галерея мебели»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 2';
    bank = 'ИНН/КПП 5012061688/504001001 р/с 40702810240040019106 в ПАО СБЕРБАНК г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистов Д.А.';
}

    var dbdate = document.getElementById('olddate').value,
        partdate = dbdate.split('-'),
        day = partdate[2],
        month = partdate[1],
        srtrmonth = strMonth(parseInt(month)),
        year = partdate[0],
        date = day + '.' + month + '.' + year,
        fullname = document.getElementById('name').innerText,
        partname = fullname.split(' '),
        famil = partname[0],
        name = (partname[1]===undefined)?'':partname[1],
        father = (partname[2]===undefined)?'':partname[2],
        sum = document.getElementById('sum').innerText.slice(0, -2),
        prep = document.getElementById('prepayment').innerText.slice(0, -2),
        dost = document.getElementById('sumdeliv').innerText.slice(0, -2),
        sbor = document.getElementById('sumcollect').innerText.slice(0, -2),
        sum1 = parseInt(sum) - parseInt(prep) + parseInt(dost),
        sum2 = parseInt(sbor),
        strsum1 = sumToString(sum1),
        strsum2 = sumToString(sum2);

    if(strsum1.length>52){
        var newstr = delitel(strsum1,52);
        var parts = newstr.split('&');
        var strsum1r1 = parts[0],
            strsum1r2 = parts[1];

    }else{
        var strsum1r1 = strsum1;
        var strsum1r2 = '';}
    if(strsum1.length>38){
        var newstr = delitel(strsum1,38);
        var parts = newstr.split('&');
        var strsum1k1 = parts[0],
            strsum1k2 = parts[1];

    }else{var strsum1k1 = strsum1, strsum1k2 = ' ';}

    if(strsum2.length>51){
        var newstr = delitel(strsum2,51);
        var parts = newstr.split('&');
        var strsum2r1 = parts[0],
            strsum2r2 = parts[1];

    }else {
        var strsum2r1 = strsum2;
        var strsum2r2 = '';}
    if(strsum2.length>38){
        var newstr = delitel(strsum2,38);
        var parts = newstr.split('&');
        var strsum2k1 = parts[0],
            strsum2k2 = parts[1];

    }else{var strsum2k1 = strsum2, strsum2k2 = ' ';}

    var dd = {
        info: {
            title:'Приходный кассовый ордер',
            author:'kittiwake'
        },
        pageSize:'A4',
        pageOrientation:'portrait',
        pageMargins:[5,5,5,5],
        content:[
            {table:{
                widths:['58%',5,'*'],
                body:[
                    [
                        {stack:[
                            {
                                text:'Унифицированная форма № КО-1\nУтверждена постановлением Госкомстата\nРоссии от 18.08.98 г. №88',
                                style:'little',
                                alignment:'right'
                            },{
                                margin:[0,4,0,0],
                                table:{
                                    widths:['*','auto',70],
                                    body:[
                                        [
                                            {
                                                text:'',
                                                colSpan:2
                                            },
                                            '',
                                            {
                                                text:'Код',
                                                style:'little',
                                                alignment:'center',
                                                border:[true, true, true, true]
                                            }
                                        ],
                                        [
                                            {text:'Форма по ОКУД',colSpan:2,style:'little',alignment:'right'},
                                            '',
                                            {text:'0310001',style:'little',alignment:'center',border:[true, true, true, true]}
                                        ],
                                        [
                                            {
                                                text: company,
                                                style:'datas',
                                                alignment:'center',
                                                border:[false, false, false, true]
                                            },
                                            {text:'по ОКПО',style:'little',alignment:'right'},
                                            {text:'',border:[true, true, true, true]}
                                        ],
                                        [
                                            {text:'(организация)\n\n',style:'under'},
                                            ' ',
                                            {text:'',border:[true, true, true, true],style:'little'}],
                                        [
                                            {
                                                text:'(структурное подразделение)',
                                                style:'under',
                                                colSpan:2,
                                                border:[false, true, false, false]
                                            },
                                            '','']
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingTop: function(i, node) {
                                        if(i === 0)
                                            return 0;
                                        else return 2;
                                    },
                                    paddingBottom: function(i, node) {
                                        return 0;
                                    }
                                }
                            },{
                                table:{
                                    widths:['*',50,55],
                                    body:[
                                        [
                                            {text:'',
                                                border:[false, false, false, false]
                                            },
                                            {text:'Номер документа',alignment:'center',style:'little'},
                                            {text:'Дата составления',alignment:'center',style:'little'}
                                        ],
                                        [
                                            {text:'ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР',
                                                border:[false, false, false, false],
                                                fontSize:10,
                                                bold:true,
                                                alignment: 'right',
                                                margin:[0,0,10,0]
                                            },
                                            {text:cont,style:'datas',bold:true},
                                            {
                                                text:date,
                                                style:'datas',bold:true
                                            }
                                        ]
                                    ],
                                    borderLines: [[0,1,0],[1,1,1],[1,1,1] ]
                                },
                                layout:{
                                    paddingLeft: function(i, node) { return 0; },
                                    paddingRight: function(i, node) { return 0; },
                                    paddingTop: function(i, node) { return 0; },
                                    paddingBottom: function(i, node) { return 0; }
                                }
                            },{
                                style:'little',
                                margin:[0,10,0,0],
                                alignment:'center',
                                table:{
                                    body:[
                                        [
                                            {text:'Дебет',rowSpan:2},
                                            {text:'Кредит',colSpan:4},
                                            '','','',
                                            {text:'Сумма,руб. коп.',rowSpan:2},
                                            {text:'Код це-левого назна-чения',rowSpan:2},
                                            {text:'',rowSpan:2}
                                        ],
                                        ['',' ',
                                            'код струк-турного подразде-ления',
                                            'корреспон-дирующий счет, субсчет',
                                            'код аналити-ческого учета',
                                            '','',''],
                                        [' ',' ',' ',' ',' ',' ',' ',
                                            {text:' ',vLineWidth:5}
                                        ]
                                    ]
                                },
                                layout: {
                                    hLineWidth: function (i, node) {
                                        return (i === 2 || i === node.table.body.length) ? 2 : 1;
                                    }
                                    // vLineWidth: function (i,j, node) {
                                    // 	return ((i === 0 || i === node.table.widths.length) && j === node.table.body.length) ? 2 : 1;
                                    // },
                                    // paddingLeft: function(i, node) { return 4; },
                                    // paddingRight: function(i, node) { return 4; },
                                    // paddingTop: function(i, node) { return 2; },
                                    // paddingBottom: function(i, node) { return 2; },
                                    // fillColor: function (i, node) { return null; }
                                }

                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        ['Принято от',
                                            {text:fullname,style:'datas',border:[false,false,false,true]},
                                        ],
                                        ['Основание:',
                                            {text:'Оплата за мебель и доставку',style:'datas',border:[false,false,false,true]},
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                margin:[0,10,0,0],
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        [{text:'Сумма',border:[false,true,false,false]},
                                            {text:strsum1r1,style:'datas',border:[false,true,false,false]}
                                        ],
                                        ['',
                                            {text:'(прописью)',style:'under',border:[false,true,false,false]},
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*','auto',12,'auto'],
                                    body:[
                                        [
                                            {text:strsum1r2,style:'datas',border:[false,false,false,true]},
                                            {text:sum1,style:'datas',border:[false,false,false,true]},
                                            'руб.',
                                            {text:'',style:'datas',border:[false,false,false,true]},
                                            'коп.'
                                        ],
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        ['В том числе',
                                            {text:'',border:[false,false,false,true]},
                                        ],
                                        ['Приложение',
                                            {text:'',border:[false,false,false,true]},
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',5,50,5,'auto'],
                                    body:[
                                        [
                                            {text:'Главный бухгалтер',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    // paddingTop: function(i, node) { return 10; },
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                },
                                margin:[0,10,0,0]
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',5,50,5,'auto'],
                                    body:[
                                        [
                                            {text:'Получил кассир',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            }
                        ],
                            width:'58%'
                        },
                        {text:'линия\n отреза',
                            style:'little',
                            margin:[0,100],
                            border:[true,false,true,false]
                        },
                        {stack:[
                            {text:'\n' + company+'\n',alignment:'center',style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {text:'(организация)\n\n\n',style:'under'},
                            {text:'КВИТАНЦИЯ\n\n\n',fontSize:10,bold:true,alignment:'center'},
                            {table:{
                                widths:['auto','*'],
                                body:[
                                    [
                                        {text:'к приходному кассовому ордеру№',style:'little'},
                                        {text:cont, style:'datas',border:[false,false,false,true]},
                                    ]
                                ]
                            },
                                layout:{
                                    // paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {table:{
                                widths:['auto',15,'auto',70,'auto','auto','auto'],
                                body:[
                                    [
                                        {text:'от "',style:'little'},
                                        {text:day,border:[false,false,false,true]},
                                        {text:'"',style:'little'},
                                        {text:srtrmonth,border:[false,false,false,true]},
                                        ' ',
                                        {text:year,border:[false,false,false,true]},
                                        {text:'г.',style:'little'}
                                    ]
                                ]
                            },
                                style:'datas',
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {columns:[
                                {text:'Принято от', style:'little', width:50},
                                [
                                    {text:famil,style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {text:name+' '+father,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {columns:[
                                {text:'Основание:', style:'little', width:50},
                                [
                                    {text:'Оплата за мебель и доставку', style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {canvas: [{ type: 'line', x1: 0, y1: 12, x2: 220, y2: 12, lineWidth: 1 }]},
                            {canvas: [{ type: 'line', x1: 0, y1: 12, x2: 220, y2:12, lineWidth: 1 }]},
                            {canvas: [{ type: 'line', x1: 0, y1: 10, x2: 220, y2: 10, lineWidth: 1 }]},
                            {table:{
                                widths:['auto',60,'auto',15,'auto'],
                                body:[
                                    [
                                        {text:'Сумма',style:'little',width:30},
                                        {text:sum1,style:'datas',border:[false,false,false,true]},
                                        {text:'руб.',style:'little',width:20},
                                        {text:'00',style:'datas',border:[false,false,false,true]},
                                        {text:'коп.',style:'little',width:50}
                                    ],
                                    ['',
                                        {text:'(цифрами)',style:'under'},
                                        '','',''
                                    ]
                                ]
                            },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                },
                                margin:[0,15,0,0]
                            },
                            {text:strsum1k1,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {text:'(прописью)',style:'under'},
                            {text:strsum1k2,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {table:{
                                widths:[80,'auto',15,'auto'],
                                body:[
                                    [
                                        {text:'',style:'datas',border:[false,false,false,true]},
                                        {text:'руб.',style:'little'},
                                        {text:'00',style:'datas',border:[false,false,false,true]},
                                        {text:'коп.',style:'little'}
                                    ]
                                ]
                            },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }

                            },
                            {columns:[
                                {text:'В том числе', style:'little', width:50},
                                [
                                    {text:' ', style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {table:{
                                widths:['auto',12,'auto',60,2,30,'auto'],
                                body:[
                                    [
                                        {text:'"',style:'little'},
                                        {text:' ',border:[false,false,false,true]},
                                        {text:'"',style:'little'},
                                        {text:'',border:[false,false,false,true]},
                                        ' ',
                                        {text:year,border:[false,false,false,true]},
                                        {text:'г.',style:'little'}
                                    ]
                                ]
                            },
                                style:'datas',
                                margin:[0,5,0,0],
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {text:'М.П. (штампа)', style:'little',margin:[20,12,0,12]},
                            {
                                style:'under',
                                table:{
                                    widths:['auto',1,40,1,'auto'],
                                    body:[
                                        [
                                            {text:'Главный бухгалтер',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',1,40,1,'auto'],
                                    body:[
                                        [
                                            {text:'Кассир',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    // paddingTop: function(i, node) { return 10; },
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            }
                        ]}
                    ]
                ]
            },
                layout:{
                    defaultBorder: false
                }
            },
            '\n\n',
            {table:{
                widths:['58%',5,'*'],
                body:[
                    [
                        {stack:[
                            {
                                text:'Унифицированная форма № КО-1\nУтверждена постановлением Госкомстата\nРоссии от 18.08.98 г. №88',
                                style:'little',
                                alignment:'right'
                            },{
                                margin:[0,4,0,0],
                                table:{
                                    widths:['*','auto',70],
                                    body:[
                                        [
                                            {
                                                text:'',
                                                colSpan:2
                                            },
                                            '',
                                            {
                                                text:'Код',
                                                style:'little',
                                                alignment:'center',
                                                border:[true, true, true, true]
                                            }
                                        ],
                                        [
                                            {text:'Форма по ОКУД',colSpan:2,style:'little',alignment:'right'},
                                            '',
                                            {text:'0310001',style:'little',alignment:'center',border:[true, true, true, true]}
                                        ],
                                        [
                                            {
                                                text: company,
                                                style:'datas',
                                                alignment:'center',
                                                border:[false, false, false, true]
                                            },
                                            {text:'по ОКПО',style:'little',alignment:'right'},
                                            {text:'',border:[true, true, true, true]}
                                        ],
                                        [
                                            {text:'(организация)\n\n',style:'under'},
                                            ' ',
                                            {text:'',border:[true, true, true, true],style:'little'}],
                                        [
                                            {
                                                text:'(структурное подразделение)',
                                                style:'under',
                                                colSpan:2,
                                                border:[false, true, false, false]
                                            },
                                            '','']
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingTop: function(i, node) {
                                        if(i === 0)
                                            return 0;
                                        else return 2;
                                    },
                                    paddingBottom: function(i, node) {
                                        return 0;
                                    }
                                }
                            },{
                                table:{
                                    widths:['*',50,55],
                                    body:[
                                        [
                                            {text:'',
                                                border:[false, false, false, false]
                                            },
                                            {text:'Номер документа',alignment:'center',style:'little'},
                                            {text:'Дата составления',alignment:'center',style:'little'}
                                        ],
                                        [
                                            {text:'ПРИХОДНЫЙ КАССОВЫЙ ОРДЕР',
                                                border:[false, false, false, false],
                                                fontSize:10,
                                                bold:true,
                                                alignment: 'right',
                                                margin:[0,0,10,0]
                                            },
                                            {text:cont,style:'datas',bold:true},
                                            {
                                                text:date,
                                                style:'datas',bold:true
                                            }
                                        ]
                                    ],
                                    borderLines: [[0,1,0],[1,1,1],[1,1,1] ]
                                },
                                layout:{
                                    paddingLeft: function(i, node) { return 0; },
                                    paddingRight: function(i, node) { return 0; },
                                    paddingTop: function(i, node) { return 0; },
                                    paddingBottom: function(i, node) { return 0; }
                                }
                            },{
                                style:'little',
                                margin:[0,10,0,0],
                                alignment:'center',
                                table:{
                                    body:[
                                        [
                                            {text:'Дебет',rowSpan:2},
                                            {text:'Кредит',colSpan:4},
                                            '','','',
                                            {text:'Сумма,руб. коп.',rowSpan:2},
                                            {text:'Код це-левого назна-чения',rowSpan:2},
                                            {text:'',rowSpan:2}
                                        ],
                                        ['',' ',
                                            'код струк-турного подразде-ления',
                                            'корреспон-дирующий счет, субсчет',
                                            'код аналити-ческого учета',
                                            '','',''],
                                        [' ',' ',' ',' ',' ',' ',' ',
                                            {text:' ',vLineWidth:5}
                                        ]
                                    ]
                                },
                                layout: {
                                    hLineWidth: function (i, node) {
                                        return (i === 2 || i === node.table.body.length) ? 2 : 1;
                                    }
                                    // vLineWidth: function (i,j, node) {
                                    // 	return ((i === 0 || i === node.table.widths.length) && j === node.table.body.length) ? 2 : 1;
                                    // },
                                    // paddingLeft: function(i, node) { return 4; },
                                    // paddingRight: function(i, node) { return 4; },
                                    // paddingTop: function(i, node) { return 2; },
                                    // paddingBottom: function(i, node) { return 2; },
                                    // fillColor: function (i, node) { return null; }
                                }

                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        ['Принято от',
                                            {text:fullname,style:'datas',border:[false,false,false,true]}
                                        ],
                                        ['Основание:',
                                            {text:'Оплата за сборку',style:'datas',border:[false,false,false,true]}
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                margin:[0,10,0,0],
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        [{text:'Сумма',border:[false,true,false,false]},
                                            {text:strsum2r1,style:'datas',border:[false,true,false,false]}
                                        ],
                                        ['',
                                            {text:'(прописью)',style:'under',border:[false,true,false,false]},
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*','auto',12,'auto'],
                                    body:[
                                        [
                                            {text:strsum2r2,style:'datas',border:[false,false,false,true]},
                                            {text:sum2,style:'datas',border:[false,false,false,true]},
                                            'руб.',
                                            {text:'',style:'datas',border:[false,false,false,true]},
                                            'коп.'
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'little',
                                table:{
                                    widths:['auto','*'],
                                    body:[
                                        ['В том числе',
                                            {text:'',border:[false,false,false,true]}
                                        ],
                                        ['Приложение',
                                            {text:'',border:[false,false,false,true]},
                                        ]
                                    ]
                                },
                                layout:{
                                    defaultBorder: false,
                                    paddingBottom: function(i, node) { return -1; }
                                }
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',5,50,5,'auto'],
                                    body:[
                                        [
                                            {text:'Главный бухгалтер',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    // paddingTop: function(i, node) { return 10; },
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                },
                                margin:[0,10,0,0]
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',5,50,5,'auto'],
                                    body:[
                                        [
                                            {text:'Получил кассир',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            }
                        ],
                            width:'58%'
                        },
                        {text:'линия\n отреза',
                            style:'little',
                            margin:[0,100],
                            border:[true,false,true,false]
                        },
                        {stack:[
                            {text:'\n'+company+'\n',alignment:'center',style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {text:'(организация)\n\n\n',style:'under'},
                            {text:'КВИТАНЦИЯ\n\n\n',fontSize:10,bold:true,alignment:'center'},
                            {table:{
                                widths:['auto','*'],
                                body:[
                                    [
                                        {text:'к приходному кассовому ордеру№',style:'little'},
                                        {text:cont, style:'datas',border:[false,false,false,true]}
                                    ]
                                ]
                            },
                                layout:{
                                    // paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {table: {
                                                        widths:['auto',15,'auto',70,'auto','auto','auto'],
                                                        body:[
                                                            [
                                                                {text:'от "',style:'little'},
                                                                {text:day, border:[false,false,false,true]},
                                                                {text:'"',style:'little'},
                                                                {text:srtrmonth, border:[false,false,false,true]},
                                                                ' ',
                                                                {text:year, border:[false,false,false,true]},
                                                                {text:'г.',style:'little'}
                                                            ]
                                                        ]
                            },
                                style:'datas',
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {columns:[
                                {text:'Принято от', style:'little', width:50},
                                [
                                    {text:famil,style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {text:name+' '+father,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {columns:[
                                {text:'Основание:', style:'little', width:50},
                                [
                                    {text:'Оплата за сборку', style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {canvas: [{ type: 'line', x1: 0, y1: 12, x2: 220, y2: 12, lineWidth: 1 }]},
                            {canvas: [{ type: 'line', x1: 0, y1: 12, x2: 220, y2:12, lineWidth: 1 }]},
                            {canvas: [{ type: 'line', x1: 0, y1: 10, x2: 220, y2: 10, lineWidth: 1 }]},
                            {table:{
                                widths:['auto',60,'auto',15,'auto'],
                                body:[
                                    [
                                        {text:'Сумма',style:'little',width:30},
                                        {text:sum2,style:'datas',border:[false,false,false,true]},
                                        {text:'руб.',style:'little',width:20},
                                        {text:'00',style:'datas',border:[false,false,false,true]},
                                        {text:'коп.',style:'little',width:50}
                                    ],
                                    ['',
                                        {text:'(цифрами)',style:'under'},
                                        '','',''
                                    ]
                                ]
                            },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                },
                                margin:[0,15,0,0]
                            },
                            {text:strsum2k1,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {text:'(прописью)',style:'under'},
                            {text:strsum2k2,style:'datas'},
                            {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 220, y2: 0, lineWidth: 1 }]},
                            {table:{
                                widths:[80,'auto',15,'auto'],
                                body:[
                                    [
                                        {text:'',style:'datas',border:[false,false,false,true]},
                                        {text:'руб.',style:'little'},
                                        {text:'00',style:'datas',border:[false,false,false,true]},
                                        {text:'коп.',style:'little'}
                                    ]
                                ]
                            },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }

                            },
                            {columns:[
                                {text:'В том числе', style:'little', width:50},
                                [
                                    {text:' ', style:'datas'},
                                    {canvas: [{ type: 'line', x1: 0, y1: 0, x2: 170, y2: 0, lineWidth: 1 }]},
                                ]
                            ]},
                            {table:{
                                widths:['auto',12,'auto',60,2,30,'auto'],
                                body:[
                                    [
                                        {text:'"',style:'little'},
                                        {text:' ',border:[false,false,false,true]},
                                        {text:'"',style:'little'},
                                        {text:'',border:[false,false,false,true]},
                                        ' ',
                                        {text:year,border:[false,false,false,true]},
                                        {text:'г.',style:'little'}
                                    ]
                                ]
                            },
                                style:'datas',
                                margin:[0,5,0,0],
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },
                            {text:'М.П. (штампа)', style:'little',margin:[20,12,0,12]},
                            {
                                style:'under',
                                table:{
                                    widths:['auto',1,40,1,'auto'],
                                    body:[
                                        [
                                            {text:'Главный бухгалтер',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            },{
                                style:'under',
                                table:{
                                    widths:['auto',1,40,1,'auto'],
                                    body:[
                                        [
                                            {text:'Кассир',style:'little'},
                                            '','','',
                                            {text:glbuh,style:'datas'},
                                        ],
                                        ['','',
                                            {text:'(подпись)',style:'under',border:[false,true,false,false]},
                                            '',
                                            {text:'(расшифровка подписи)',style:'under',border:[false,true,false,false]}
                                        ]
                                    ]
                                },
                                layout:{
                                    // paddingTop: function(i, node) { return 10; },
                                    paddingBottom: function(i, node) { return -1; },
                                    defaultBorder: false
                                }
                            }
                        ]}
                    ]
                ]
            },
                layout:{
                    defaultBorder: false
                }
            },

        ],
        styles:{
            little:{
                fontSize:8
            },
            under:{
                fontSize:5,
                alignment:'center'
            },
            datas:{
                fontSize:10,
                alignment:'center',
                italics: true
            }
        }
    };

    pdfMake.createPdf(dd).open();
}

function torg12(){
    
    var ooo, company,uraddr,bank;
    ooo = document.getElementById('ooo').value;
    
switch (ooo) {
  case 'gm':
    company = 'ООО «Галерея мебели»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 2';
    bank = 'ИНН/КПП 5012061688/504001001 р/с 40702810240040019106 в ПАО СБЕРБАНК г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистов Д.А.';
    break;
  case 'als':
    company = 'ООО «Александрия»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 3';
    bank = 'ИНН/КПП 5041202326/504001001 ОГРН 1155012001671 ОКТМО 47664000 р/с 40702810140000007326 в ПАО "Сбербанк России" г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистова Н.П.';
    break;
  case 'mk':
    company = ' ИП БАРЛАДЯН ЕВГЕНИЙ ВАСИЛЬЕВИЧ';
    uraddr = '141851 Дмитровский р-н дер. Голявино д.35';
    bank = 'ИНН 502480559844\nОГРНИП 313500734000015 ОКТМО 46608101166 р/с 40802810802640002367 в АО "АЛЬФА-БАНК" г.Москва БИК 044525593 \nк/с 30101810200000000593';
    glbuh = 'Барладян Е.В.';
    break;
  default:
    company = 'ООО «Галерея мебели»';
    uraddr = '140143, Московская область, г.о. Раменский, рп Родники, ул. Седовцев, д. 11А, офис 2';
    bank = 'ИНН/КПП 5012061688/504001001 р/с 40702810240040019106 в ПАО СБЕРБАНК г.Москва БИК 044525225 к/с 30101810400000000225';
    glbuh = 'Чистов Д.А.';
}

    var cont = document.getElementById('zakaz').innerText,
        datacon = document.getElementById('datacon').innerText,
        osnov = 'Договор № '+cont+' от '+datacon + ' на поставку мебели по индивидуальному заказу';
    //дату не сегодня, а дату плановую
    var dbdate = document.getElementById('olddate').value,
        partdate = dbdate.split('-'),
        day = partdate[2],
        month = partdate[1],
        srtrmonth = strMonth(parseInt(month)),
        year = partdate[0],
        date = day + '.' + month + '.' + year,
        fullname = document.getElementById('name').innerText,
        address = document.getElementById('adress').innerText,
        customer = fullname + '. '+address,
        //partname = fullname.split(' '),
        //famil = partname[0],
        //name = (partname[1]===undefined)?'':partname[1],
        //father = (partname[2]===undefined)?'':partname[2],
        sum = document.getElementById('sum').innerText.slice(0, -2),
        //prep = document.getElementById('prepayment').innerText.slice(0, -2),
        //dost = document.getElementById('sumdeliv').innerText.slice(0, -2),
        //sbor = document.getElementById('sumcollect').innerText.slice(0, -2),
        //sum1 = parseInt(sum) - parseInt(prep) + parseInt(dost),
        //sum2 = parseInt(sbor),
        //strsum1 = sumToString(sum1),
        strsum = sumToString(sum);
    if(strsum.length>48){
        var newstr = delitel(strsum,48);
        var parts = newstr.split('&');
        var strsum1 = parts[0],
            strsum2 = parts[1];

    }else{var strsum1 = strsum; var strsum2 = '';}
    //if(strsum1.length>38){
    //    var newstr = delitel(strsum1,38);
    //    var parts = newstr.split('&');
    //    var strsum1k1 = parts[0],
    //        strsum1k2 = parts[1];
    //
    //}else{var strsum1k1 = strsum1, strsum1k2 = ' ';}

    //if(strsum2.length>51){
    //    var newstr = delitel(strsum2,52);
    //    var parts = newstr.split('&');
    //    var strsum2r1 = parts[0],
    //        strsum2r2 = parts[1];
    //
    //}else{var strsum2r1 = strsum2; var strsum2r2 = '';}
    //if(strsum2.length>38){
    //    var newstr = delitel(strsum2,38);
    //    var parts = newstr.split('&');
    //    var strsum2k1 = parts[0],
    //        strsum2k2 = parts[1];
    //
    //}else{var strsum2k1 = strsum2, strsum2k2 = ' ';}

    var dd = {
        info: {
            title:'Товарная накладная',
            author:'kittiwake'
        },
        pageSize:'A4',
        pageOrientation:'landscape',
        pageMargins:[5,5,5,5],
        content:[
            {text:'Унифицированная форма № ТОРГ-12',alignment:'right'},
            {text:'Утверждена постановлением Госкомстата',alignment:'right'},
            {text:'России от 25.12.98 № 132',alignment:'right'},
            {table:{
                widths:['auto','*',30,60],
                body:[
                    [
                        {text:'',colSpan:3,border:[false,false,false,false]},
                        '',
                        '',
                        {text:'Код',alignment:'center'}
                    ],[
                        {text:'Форма по ОКУД',colSpan:3,border:[false,false,false,false],alignment:'right'},
                        '',
                        '',
                        {text:'0330212',style:'datas'}
                    ],
                    [
                        {
                            text: company + ' ' + uraddr,
                            colSpan:2,
                            border:[false,false,false,true],
                            style:'datas'
                        },
                        '',
                        {
                            text:'по ОКПО',
                            border:[false,false,false,false]
                        },
                        {text:'66156318',style:'datas'}
                    ],[
                        {
                            text:'организация – грузоотправитель, адрес, номер телефона, факса, банковские реквизиты',
                            colSpan:2,
                            border:[false,false,false,false],
                            style:'under'
                        },
                        '',
                        {text:' ',border:[false],style:'little'},
                        ''
                    ],[
                        {text:'',border:[false,true]},
                        {columns:[
                            {text:'структурное подразделение',style:'under'},
                            {text:'Вид деятельности',alignment:'right'}
                        ],border:[false,true]},
                        {text:'по ОКДП',border:[false,true]},
                        ''
                    ],[
                        {text:'Грузополучатель',border:[false]},
                        {
                            text:customer,
                            border:[false,false,false,true],
                            style:'datas'
                        },
                        {
                            text:'по ОКПО',
                            border:[false]
                        },
                        {text:'',rowSpan: 2}
                    ],[
                        {text:'',border:[false]},
                        {
                            text:'наименование организации, адрес, номер телефона, банковские реквизиты',
                            border:[false,false,false,false],
                            style:'under'
                        },
                        {text:'',border:[false]},
                        ''
                    ],[
                        {text:'Поставщик',border:[false]},
                        {
                            text: company + ' ' + uraddr + ' ' + bank,
                            border:[false,false,false,true],
                            style:'datas'
                        },
                        {text:'по ОКПО',border:[false]},
                        ''
                    ],[
                        {text:'Плательщик',border:[false]},
                        {
                            text:customer,
                            border:[false,false,false,true],
                            style:'datas'
                        },
                        {text:'по ОКПО',border:[false]},
                        {text:'',rowSpan:2}
                    ],[
                        {text:'',border:[false]},
                        {
                            text:'наименование организации, адрес, номер телефона, банковские реквизиты',
                            border:[false,false,false,false],
                            style:'under'
                        },
                        {text:'',border:[false]},
                        ''
                    ],[
                        {text:'Основание',border:[false]},
                        {
                            text:osnov,
                            border:[false,false,false,true],
                            style:'datas'
                        },
                        {text:'номер',alignment:'right'},
                        ''
                    ],[
                        {text:'',border:[false]},
                        {
                            text:'наименование документа (договор, контракт, заказ-наряд)',
                            border:[false,false,false,false],
                            style:'under'
                        },
                        {text:'дата',alignment:'right'},
                        ''
                    ],[
                        {text:'',border:[false]},
                        {
                            text:'Транспортная накладная',
                            border:[false],
                            alignment:'right'
                        },
                        {text:'номер',alignment:'right'},
                        ''
                    ],[
                        {text:'',border:[false]},
                        {text:'',border:[false]},
                        {text:'дата',alignment:'right'},
                        ''
                    ],[
                        {text:'',border:[false]},
                        {text:'Вид операции',border:[false],alignment:'right'},
                        {text:'',border:[false]},
                        'доставка'
                    ]
                ]
            }},
            {table:{
                body:[
                    [
                        {text:'',border:[false]},
                        'Номер документа',
                        'Дата составления'
                    ],[
                        {text:'ТОВАРНАЯ НАКЛАДНАЯ',border:[false],bold:true,fontSize:12},
                        {text:cont,style:'datas',bold:true},
                        {text:date,style:'datas',bold:true}
                    ]
                ]
            },
                margin:[30,-30,0,20]
            },
            {table:{
                body:[[
                    {text:'Но-мер по по-рядку',rowSpan:2},
                    {text:'Товар', colSpan: 2},
                    '',
                    {text:'Единица измерения',colSpan: 2},
                    '',
                    {text:'Вид упаков-ки',rowSpan:2},
                    {text:'Количество',colSpan: 2},
                    '',
                    {text:'Масса брутто',rowSpan:2},
                    {text:'Количест-во (масса нетто)',rowSpan:2},
                    {text:'Цена, руб. коп',rowSpan:2},
                    {text:'Сумма без учета НДС, руб. коп',rowSpan:2},
                    {text:'НДС',colSpan: 2},
                    '',
                    {text:'Сумма с учетом НДС, руб. коп',rowSpan:2}
                ],
                    [
                    '',
                    'наименование, характеристика, сорт, артикул товара',
                    'код',
                    'наиме-нование',
                    'код по ОКЕИ',
                    '',
                    'в одном месте',
                    'мест, штук',
                    '',
                    '',
                    '',
                    '',
                    'ставка, %',
                    'сумма, руб. коп',
                    ''
                ],[
                    '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'
                ],[
                    {text:'1',style:'datas'},
                    {text:'Мебель',style:'datas'},
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    {text:sum,style:'datas'},
                    {text:sum,style:'datas'},
                    '',
                    '',
                    {text:sum,style:'datas'}
                ],[
                    {text:'16Итого',colSpan:7,alignment:'right'},
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    {text:'X',style:'datas'},
                    '',
                    {text:'X',style:'datas'},
                    '',
                    {text:sum,style:'datas'}
                ]]
            },
                style:'litcentr'
            },
            {table:{
                widths:['auto',320,'auto'],
                body:[[
                    'Товарная накладная имеет приложение на',
                    {text:'',border:[false,false,false,true]},
                    'листах'
                ]]
            },
                layout:{
                    defaultBorder: false
                }
            },
            {table:{
                widths:['auto',480,'auto'],
                body:[[
                    'и содержит',
                    {text:'один',style:'datas'},
                    'порядковых номеров записей'
                ],[
                    '',
                    {text:'прописью',style:'under',border:[false,true]},
                    ''
                ]]
            },
                layout:{
                    defaultBorder: false
                }
            },
            {table:{
                widths:['auto',180,'auto',270,'*'],
                body:[
                    [
                    '',
                    '',
                    'Масса груза (нетто)',
                    '',
                    {text:'',border:[true,true,true,true]}
                ],[
                    'Всего мест',
                    '',
                    'Масса груза (брутто)',
                    {text:'прописью',style:'under',border:[false,true]},
                    {text:'',border:[true,true,true,true]}
                ],[
                    '',
                    {text:'прописью',style:'under',border:[false,true]},
                    '',
                    {text:'прописью',style:'under',border:[false,true]},
                    ''
                ]
                ]
            },
                layout:{
                    defaultBorder: false
                }
            },
            {table:{
                widths:['50%','*'],
                body:[[
                    {stack:[
                        {table:{
                            widths:['auto',50,'auto'],
                            body:[[
                                'Приложение (паспорта, сертификаты, и т.п.) на',
                                {text:'',border:[false,false,false,true]},
                                'листах'
                            ],[
                                '',
                                {text:'прописью',style:'under'},
                                ''
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:['auto','*','auto','auto','auto'],
                            body:[[
                                'Всего отпущено на сумму',
                                {text:strsum1,style:'datas',border:[false,false,false,true],colSpan:3},
                                '','',''
                            ],[
                                '',
                                {text:strsum2,style:'datas',border:[false,false,false,true]},
                                'руб.',
                                {text:'00',style:'datas',border:[false,false,false,true]},
                                'коп.'
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:['*','auto',5,40,5,80],
                            body:[[
                                'Отпуск разрешил',
                                {text:'Ген.директор',style:'datas',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:glbuh,style:'datas',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'должность',style:'under'},
                                '',
                                {text:'подпись',style:'under'},
                                '',
                                {text:'расшифровка подписи',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:['*',40,5,80],
                            body:[[
                                'Главный (старший) бухгалтер',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:glbuh,style:'datas',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'подпись',style:'under'},
                                '',
                                {text:'расшифровка подписи',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:['*','auto',5,40,5,80],
                            body:[[
                                'Отпуск груза произвел',
                                {text:'Ген.директор',style:'datas',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:glbuh,style:'datas',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'должность',style:'under'},
                                '',
                                {text:'подпись',style:'under'},
                                '',
                                {text:'расшифровка подписи',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:[80,'auto',20,'auto',70,5,'auto','auto'],
                            body:[[
                                'М.П.',
                                '“',
                                {text:day,border:[false,false,false,true],style:'datas'},
                                '”',
                                {text:srtrmonth,border:[false,false,false,true],style:'datas'},
                                '',
                                {text:year,border:[false,false,false,true],style:'datas'},
                                'года'
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        }
                    ]},
                    {stack:[
                        {table:{
                            widths:['auto',60,'auto',20,'auto',80,3,25,'auto'],
                            body:[[
                                'По доверенности №',
                                {text:'',border:[false,false,false,true]},
                                'от“',
                                {text:'',border:[false,false,false,true]},
                                '”',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]},
                                'года'
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }},
                        {table:{
                            widths:['auto','*'],
                            body:[[
                                '\nвыданной',
                                {text:'',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'кем, кому (организация, должность, фамилия, и., о.)',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }},
                        {canvas:[{
                            type:'line',
                            x1: 0, y1: 12, x2: 400, y2: 12
                        }]},
                        {canvas:[{
                            type:'line',
                            x1: 0, y1: 18, x2: 400, y2: 18
                        }]},
                        {table:{
                            widths:['*',80,5,40,5,80],
                            body:[[
                                'Груз принял',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'должность',style:'under'},
                                '',
                                {text:'подпись',style:'under'},
                                '',
                                {text:'расшифровка подписи',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }},
                        {table:{
                            widths:['*',80,5,40,5,80],
                            body:[[
                                'Груз получил грузополучатель',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:'',border:[false,false,false,true]}
                            ],[
                                '',
                                {text:'должность',style:'under'},
                                '',
                                {text:'подпись',style:'under'},
                                '',
                                {text:'расшифровка подписи',style:'under'}
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        },
                        {table:{
                            widths:[80,'auto',20,'auto',70,5,'auto','auto'],
                            body:[[
                                'М.П.',
                                '“',
                                {text:'',border:[false,false,false,true]},
                                '”',
                                {text:'',border:[false,false,false,true]},
                                '',
                                {text:year,border:[false,false,false,true],style:'datas'},
                                'года'
                            ]]
                        },
                            layout: {
                                defaultBorder: false
                            }
                        }
                    ]}
                ]]
            },
                layout: {
                    vLineWidth: function (i, node) {
                        return (i === 0 || i === node.table.widths.length) ? 0 : 1;
                    },
                    hLineWidth: function () {
                        return 0;
                    }
                },
                margin:[0,10,0,0]
            }
        ],
        styles:{
            little:{
                fontSize:8
            },
            litcentr:{
                fontSize:8,
                alignment:'center'
            },
            under:{
                fontSize:5,
                alignment:'center',
                margin:[0,-2]
            },
            datas:{
                fontSize:10,
                alignment:'center',
                italics: true,
                margin:[0,0,0,-3]
            }
        },
        defaultStyle: {
            fontSize:7
        }
    };


    pdfMake.createPdf(dd).open();
}