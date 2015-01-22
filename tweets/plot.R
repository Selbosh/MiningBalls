tweets <-  read.csv('136836.csv')
attach(tweets)
plot(time,
		lowess(time,sentiment,f=0.01)$y,
		col='red',
		type='l',
		ylab='Tweet sentiment',
		main='West Bromwich Albion vs. Everton',
		ylab='Time')

#Start and endpoints
abline(v=as.POSIXct("21:03", format="%H:%M"))
abline(v=as.POSIXct("20:01", format="%H:%M"))
abline(v=as.POSIXct("20:50", format="%H:%M"))
abline(v=as.POSIXct("21:52", format="%H:%M"))
		
#Penalty awarded to Everton and penalty missed
abline(v=as.POSIXct("20:47 19", format="%H:%M %d"), lty=2, col='green')
abline(v=as.POSIXct("20:49 19", format="%H:%M %d"), lty=2, col='green')

#summary stats
mean(sentiment[(sentiment< -3)|(sentiment>3)])