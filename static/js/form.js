$(function() {

    $('#submit').click(function(event) {

        $.ajax({

            data: {
                userResponse: $("#userResponse").val()
            },
            type: 'POST',
            dataType: 'json',
            url: '/chat',
            success: function(data) {

                // $("#temp").append("<br><br><br>hi")

                u = "<div class='alert alert-primary right w40r'>";
                $("#temp").append(u + data.userResponse + "</div>");
                o = "<br><br><br> <div class='alert alert-secondary left w40l'>";


                if (data.type == 'default') {

                    setTimeout(function() {
                        $("#temp").append(o + data.output + "</div><br><br><br>")
                    }, 150);

                } else if (data.type == 'event') {

                    var ev = '';
                    var br = '';
                    for (i = 0; i < data.eNames.length; i++) {
                        ev = ev + data.eNames[i] + ' occuring on ' + data.eTimes[i] + '<br>';
                        br = br + '<br>'
                    }
                    setTimeout(function() {
                        $("#temp").append(o + data.output + '<br>' + ev + "</div><br><br><br>" + br)
                    }, 150);

                } else if (data.type == 'holiday') {

                    var hol = ''
                    var br = ''
                    for (i = 0; i < data.holIdx.length; i++) {
                        hol = hol + data.calDate[data.holIdx[i]] + '<br>';
                        br = br + '<br>';
                    }
                    setTimeout(function() {
                        $("#temp").append(o + data.output + '<br>' + hol + "</div><br><br><br>" + br)
                    }, 150);

                } else if (data.type == 'result') {

                    var res = data.calDate[data.resIdx];
                    setTimeout(function() {
                        $("#temp").append(o + data.output + ' ' + res + "</div>")
                    }, 150);

                } else if (data.type == 'facError') {

                    setTimeout(function() {
                        $("#temp").append(o + ' ' + data.name + data.output + "</div><br><br><br>")
                    }, 150);

                } else if (data.type == 'dmail') {

                    var de = 'Email- ' + data.email + '<br>' + data.name + ': ' + data.desg;
                    setTimeout(function() {
                        $("#temp").append(o + de + "</div><br><br><br><br>")
                    }, 150);

                } else if (data.type == 'email') {

                    var e = data.name + ': ' + 'Email- ' + data.email;
                    setTimeout(function() {
                        $("#temp").append(o + e + "</div><br><br><br>")
                    }, 150);

                } else if (data.type == 'desg') {

                    var d = data.name + ': ' + data.desg;
                    setTimeout(function() {
                        $("#temp").append(o + d + "</div><br><br><br>")
                    }, 150);

                }

            },

            error: function(error) {
                console.error(error)
            }
        });
        event.preventDefault();
    });

});