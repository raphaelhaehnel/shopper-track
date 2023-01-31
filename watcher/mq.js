const amqp = require("amqplib/callback_api")

module.exports = callback => amqp.connect("amqp://localhost", function (err, conn) {
    if (err) {
        console.error(err)
    } else {
        conn.createChannel(function (err, ch) {
            if (err) {
                console.error(err)
            } else {
                callback(ch)
            }
        })
    }
})

process.on('exit', () => {
    ch.close();
    console.log(`Closing rabbitmq channel`);
})