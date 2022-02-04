function initialize() {
    var latlng = new google.maps.LatLng(35.433043, 139.9289269);
    var opts = {
        zoom: 10,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.SATELLITE,
        mapTypeControl: false, //マップタイプ コントロール
        zoomControl: false,
        streetViewControl: false,
        RotateControl: false,
        scaleControll: false,
        fullscreenControl: false,
    };
    map = new google.maps.Map(document.getElementById("map"), opts);

    const myLatLng1 = { lat: 35.5690285, lng: 140.0321934 };
    new google.maps.Marker({
        position: myLatLng1,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '千葉港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    // Event
    map.addListener("click", function (argument) {
        console.log(argument);
    });

    const myLatLng2 = { lat: 35.5895168, lng: 139.7944278 };
    new google.maps.Marker({
        position: myLatLng2,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '東京港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    const myLatLng3 = { lat: 35.4914654, lng: 139.774088 };
    new google.maps.Marker({
        position: myLatLng3,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '川崎港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    const myLatLng4 = { lat: 35.3910755, lng: 139.6501657 };
    new google.maps.Marker({
        position: myLatLng4,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '横浜港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    const myLatLng5 = { lat: 35.2732775, lng: 139.7014765 };
    new google.maps.Marker({
        position: myLatLng5,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '横須賀港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    const myLatLng6 = { lat: 35.3748435, lng: 139.8345594 };
    new google.maps.Marker({
        position: myLatLng6,
        map,
        icon: {
            url: '',
            size: new google.maps.Size(1, 1)
        },
        label: {
            text: '木更津港',
            color: '#ffffff',
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            fontSize: '13px'
        }
    });

    //千葉港
    var flightPlanCoordinates1 = [
        //千葉港1
        new google.maps.LatLng(35.6716608, 139.9531405),
        new google.maps.LatLng(35.5267095, 139.9309341),
        //千葉港2
        new google.maps.LatLng(35.5267095, 139.9309341),
        new google.maps.LatLng(35.4560869, 139.9511383)
    ];
    //ポリライン
    var flightPath1 = new google.maps.Polyline({
        path: flightPlanCoordinates1,
        //色
        strokeColor: "#ffffff",
        //透明度
        strokeOpacity: 1.0,
        //太さ
        strokeWeight: 1.5
    });

    //東京港
    var flightPlanCoordinates2 = [
        //東京港1
        new google.maps.LatLng(35.6124553, 139.8355183),
        new google.maps.LatLng(35.5762447, 139.8362859),
        //東京港2
        new google.maps.LatLng(35.5762447, 139.8362859),
        new google.maps.LatLng(35.5145171, 139.82347),
        //東京港3
        new google.maps.LatLng(35.5145171, 139.82347),
        new google.maps.LatLng(35.5321267, 139.7949308)
    ];
    //ポリライン
    var flightPath2 = new google.maps.Polyline({
        path: flightPlanCoordinates2,
        strokeColor: "#ffffff",
        strokeOpacity: 1.0,
        strokeWeight: 1.5
    });

    //川崎港
    var flightPlanCoordinates3 = [
        //川崎港1
        new google.maps.LatLng(35.5145171, 139.82347),
        new google.maps.LatLng(35.4957272, 139.8410569),
        //川崎港2
        new google.maps.LatLng(35.4400103, 139.7657658),
        new google.maps.LatLng(35.4697497, 139.7253946),
        //川崎港3
        new google.maps.LatLng(35.4697497, 139.7253946),
        new google.maps.LatLng(35.4906952, 139.7114917)
    ];
    //ポリライン
    var flightPath3 = new google.maps.Polyline({
        path: flightPlanCoordinates3,
        strokeColor: "#ffffff",
        strokeOpacity: 1.0,
        strokeWeight: 1.5
    });

    //横浜港
    var flightPlanCoordinates4 = [
        //横浜港1
        new google.maps.LatLng(35.4650207, 139.7290949),
        new google.maps.LatLng(35.3281358, 139.6593661),
        //横浜港2
        new google.maps.LatLng(35.3281358, 139.6593661),
        new google.maps.LatLng(35.3312124, 139.6222787)
    ];
    //ポリライン
    var flightPath4 = new google.maps.Polyline({
        path: flightPlanCoordinates4,
        strokeColor: "#ffffff",
        strokeOpacity: 1.0,
        strokeWeight: 1.5
    });

    //横須賀港
    var flightPlanCoordinates5 = [
        //横須賀港1
        new google.maps.LatLng(35.3281358, 139.6593661),
        new google.maps.LatLng(35.2680073, 139.7618787),
        //横須賀港2
        new google.maps.LatLng(35.2680073, 139.7618787),
        new google.maps.LatLng(35.2139865, 139.7379643),
        //横須賀港3
        new google.maps.LatLng(35.2139865, 139.7379643),
        new google.maps.LatLng(35.2204318, 139.7133413)
    ];
    //ポリライン
    var flightPath5 = new google.maps.Polyline({
        path: flightPlanCoordinates5,
        strokeColor: "#ffffff",
        strokeOpacity: 1.0,
        strokeWeight: 1.5
    });

    //木更津港
    var flightPlanCoordinates6 = [
        //木更津港1
        new google.maps.LatLng(35.3144158, 139.8044559),
        new google.maps.LatLng(35.3766634, 139.7605604),
        //木更津港2
        new google.maps.LatLng(35.3766634, 139.7605604),
        new google.maps.LatLng(35.4043653, 139.7677423),
        //木更津港3
        new google.maps.LatLng(35.4043653, 139.7677423),
        new google.maps.LatLng(35.4359917, 139.8310179),
        //木更津港4
        new google.maps.LatLng(35.4359917, 139.8310179),
        new google.maps.LatLng(35.408254, 139.8988681)
    ];
    //ポリライン
    var flightPath6 = new google.maps.Polyline({
        path: flightPlanCoordinates6,
        strokeColor: "#ffffff",
        strokeOpacity: 1.0,
        strokeWeight: 1.5
    });

    // function map_canvas() {
    //マーカーの情報
    var data = new Array();
    data.push({
        //千葉港
        lat: '35.5790285', //緯度
        lng: '140.0321934', //経度
        url: 'https://www.pref.chiba.lg.jp/kouwan/chibanokouwan/chiba/' //リンク先(awsエンドポイントを記入)
    });
    data.push({
        //東京港
        lat: '35.5995168',
        lng: '139.7944278',
        url: 'https://www.kouwan.metro.tokyo.lg.jp/'
        
    });
    data.push({
        //川崎港
        lat: '35.5014654',
        lng: '139.774088',
        url: 'https://www.city.kawasaki.jp/kurashi/category/29-6-0-0-0-0-0-0-0-0.html'
    });
    data.push({
        //横浜港
        lat: '35.4010755',
        lng: '139.6501657',
        url: 'https://www.city.yokohama.lg.jp/city-info/yokohamashi/yokohamako/port_of_yokohama.html'
    });
    data.push({
        //横須賀港
        lat: '35.2832775',
        lng: '139.7014765',
        url: 'https://www.city.yokosuka.kanagawa.jp/6620/minato/index.html'
    });
    data.push({
        //木更津港
        lat: '35.3848435',
        lng: '139.8345594',
        url: 'https://www.pref.chiba.lg.jp/kouwan/chibanokouwan/kisarazu.html'
    });

    //初期位置に、上記配列の一番初めの緯度経度を格納
    var latlng = new google.maps.LatLng(data[0].lat, data[0].lng);

    //マーカーを配置するループ
    for (i = 0; i < data.length; i++) {
        var markers = new google.maps.Marker({
            position: new google.maps.LatLng(data[i].lat, data[i].lng),
            map: map
        });
        //クリックしたら指定したurlに遷移するイベント
        google.maps.event.addListener(markers, 'click', (function (url) {
            return function () { location.href = url; };
        })(data[i].url));
    }


    //地図描画を実行
    // google.maps.event.addDomListener(window, 'load', map_canvas);

    flightPath1.setMap(map);
    flightPath2.setMap(map);
    flightPath3.setMap(map);
    flightPath4.setMap(map);
    flightPath5.setMap(map);
    flightPath6.setMap(map);


}
