const parse_video_file = file => file.toString().split("\n").map(line => {
    const [frame, _, x, y, w, h] = line.split(" ")
    return {
        frame,
        x: parseInt(x),
        y: parseInt(y),
        w: parseInt(w),
        h: parseInt(h),
    }
}).slice(0, -1).map(({ frame, x, y, w, h }) => ({
    frame,
    x: x + w / 2,
    y: y + h
})).reduce((acc, val) => {
    if (!acc[val.frame]) {
        acc[val.frame] = []
    }
    acc[val.frame].push({ x: val.x, y: val.y })
    return acc
}, {})

// const parsed_video_file = parse_video_file(video_file)
// fs.writeFileSync(`${file_path.substring(0, file_path.lastIndexOf("."))}_parsed.json`, JSON.stringify(parsed_video_file))

module.exports = parse_video_file