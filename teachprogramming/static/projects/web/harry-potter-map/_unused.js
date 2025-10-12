const img_foot = new Image()
img_foot.src = urlParams.get('foot') || "static/foot.png"


function pos_pair_to_angle(x1,y1, x2,y2) {
    return Math.atan2(y2-y1, x2-x1)
}

function drawFoot(x,y,angle,step_count) {
    //ctx.fillRect(x, y, 8,8)
    const scale = 0.5
    const t = ctx.getTransform()
    ctx.translate(x,y)
    ctx.rotate(angle+Math.PI/2)
    if (step_count%2==0) {ctx.scale( 1, 1); ctx.translate(-img_foot.width/2,0);} //ctx.translate(img_foot.width,0)
    else                 {ctx.scale(-1, 1);}
    ctx.scale(scale, scale)
    ctx.drawImage(img_foot, -img_foot.width/2, -img_foot.height/2)
    ctx.setTransform(t)
}
