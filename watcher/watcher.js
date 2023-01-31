const fs = require("fs")
const parse = require("./mot_parser")
const mq = require("./mq")

mq((ch) => {
    let hasRenamed = false

    fs.watch("./out", async (event, filename) => {
        if (hasRenamed) return

        if (!fs.existsSync(`./out/${filename}`)) return

        hasRenamed = true
        console.log("renaming", filename)

        fs.renameSync(`./out/${filename}`, `./parsed/${filename}`, error => {
            if (error) console.error(error)
        })

        const video_file = fs.readFileSync(`./parsed/${filename}`)
        const parsed_video_file = JSON.stringify(parse(video_file))
        const buffer = Buffer.alloc(parsed_video_file.length)
        buffer.write(parsed_video_file)
        ch.sendToQueue("coords", buffer)

        setTimeout(() => hasRenamed = false, 5000)
    })
})