$(function(){
    var index=0
    var timer = setInterval(autoPlay,4000);
    var imgs=["PhoneInsider01.png","PhoneInsider02.png","PhoneInsider03.png","PhoneInsider04.png"]
    var IcoY=["animate01.Ico.png","animate02.Ico.png","animate03.Ico.png","animate04.Ico.png"]
    var Ico=["animate01.Ico.Yellow.png","animate02.Ico.Yellow.png","animate03.Ico.Yellow.png","animate04.Ico.Yellow.png"]
    /////////////////////////////////////////////////////////////
    function autoPlay(){
        $(".WillNotComeOut").each(function(){
            $(this).css({"color":"black","transform":"scale(1)"})
        });
        $(".animate01LiListers:last-child").each(function(){
            $(this).css({"color":"grey","font-size":"16px"})
        });
        index = ++ index == $(".animateIcoLi").length ? 0:index;
        $(".WillNotComeOut").eq(index).css({
            "color":"#FFBA1E",
            "transform":"scale(1.5)"
        });
        $(".animate01LiListers:last-child").eq(index).css({
            "color":"#FFBA1E"
        });
        $(".PhoneContents").css({
            "background-image":"url('./imgs/"+imgs[index]+"')"
        })
    }
    //////////////////////////////////////////////////////////////
    $(".animateIcoLi").bind("mouseover",function(){
        clearInterval(timer)
        $(".WillNotComeOut").each(function(){
            $(this).css({"transform":"scale(1)","color":"black"})
        })
        $(".animate01LiListers:last-child").each(function(){
            $(this).css({"color":"grey"})
        })
        console.log("进入")
    });
    $(".animateIcoLi").bind("mouseout",function(){
        timer = setInterval(autoPlay,4000)
        console.log("出去")
    });

    $(".animateIcoLi").eq(0).bind("mouseover",function(){
        $(".PhoneContents").css({"background-image":"url('./imgs/"+imgs[0]+"')"})
        $(".microIco").eq(0).css({"background-image":"url('./imgs/"+Ico[0]+"')"})
    });
    $(".animateIcoLi").eq(1).bind("mouseover",function(){
        $(".PhoneContents").css({"background-image":"url('./imgs/"+imgs[1]+"')"})
        $(".microIco").eq(1).css({"background-image":"url('./imgs/"+Ico[1]+"')"})
    });
    $(".animateIcoLi").eq(2).bind("mouseover",function(){
        $(".PhoneContents").css({"background-image":"url('./imgs/"+imgs[2]+"')"})
        $(".microIco").eq(2).css({"background-image":"url('./imgs/"+Ico[2]+"')"})
    });
    $(".animateIcoLi").eq(3).bind("mouseover",function(){
        $(".PhoneContents").css({"background-image":"url('./imgs/"+imgs[3]+"')"})
        $(".microIco").eq(3).css({"background-image":"url('./imgs/"+Ico[3]+"')"})
    });
    ///////////outoutoutoutout////////////////////

    $(".animateIcoLi").eq(0).bind("mouseout",function(){
        $(".microIco").eq(0).css({"background-image":"url('./imgs/"+IcoY[0]+"')"})
    });
    $(".animateIcoLi").eq(1).bind("mouseout",function(){
        $(".microIco").eq(1).css({"background-image":"url('./imgs/"+IcoY[1]+"')"})
    });
    $(".animateIcoLi").eq(2).bind("mouseout",function(){
        $(".microIco").eq(2).css({"background-image":"url('./imgs/"+IcoY[2]+"')"})
    });
    $(".animateIcoLi").eq(3).bind("mouseout",function(){
        $(".microIco").eq(3).css({"background-image":"url('./imgs/"+IcoY[3]+"')"})
    });
});