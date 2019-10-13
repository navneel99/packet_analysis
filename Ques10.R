library("fitdistrplus")

ia_packet_times <- read.csv("Q71.csv")$X  #or whatever column name you have Question 7 output
ia_conn_times <- read.csv("Q61.csv")$X 

head(ia_packet_times)

png(filename = "q10_packet_dist_day1.png")
plotdist(ia_packet_times, histo=TRUE, demp=TRUE)
dev.off()

png(filename = "q10_conn_dist_day1.png")
plotdist(ia_conn_times, histo=TRUE, demp=TRUE) 
dev.off()
png(filename = "q10_outliers_packet_day1.png")
descdist(ia_packet_times) 
dev.off()
png(filename="q10_outliers_conn_day1.png")
descdist(ia_conn_times) 
dev.off()


par(mfrow=c(2,2))
fe <- fitdist(ia_packet_times, "norm")
fe
# Fitting of the distribution ' exp ' by maximum likelihood 
# Parameters:
#   estimate  Std. Error
# rate 0.8827282 0.003196629
plot(fe)
# denscomp(list(fe), legendtext=c("exp"))
# cdfcomp(list(fe), legendtext=c("exp"))
# qqcomp(list(fe), legendtext=c("exp"))

par(mfrow=c(2,2))
fe <- fitdist(ia_conn_times, "exp")
fe
# Fitting of the distribution ' exp ' by maximum likelihood 
# Parameters:
#   estimate   Std. Error
# rate 0.01883835 0.0004657142
plot(fe)
# denscomp(list(fe), legendtext=c("exp"))
# cdfcomp(list(fe), legendtext=c("exp"))
# qqcomp(list(fe), legendtext=c("exp"))


# Question 11

queue_size <- function (lambda, mu) {
  return (lambda/(mu - lambda))
}

waiting_time <- function (lambda, mu) {
  return(1/(mu - lambda) - 1/mu)
}

# Mean packet size for day 1 from server = 248.5 bits
# Mean packet size for day 1 from client = 100.5 bits

# From server (ia_packet)
# lambda = 0.8827282
# mu = packets/second = 1/0.0019 = 515.0906 
# rho = 0.001713734
# N = 0.001716676
# W = 3.332765e-06
mu1 <- 515.0906
ggplot(mapping = aes(seq(0, mu1, 2), queue_size(seq(0, mu1, 2), mu1))) + geom_line() + xlab("lambda") + ylab("queue_size")
ggplot(mapping = aes(seq(0, mu1, 2), waiting_time(seq(0, mu1, 2), mu1))) + geom_line() + xlab("lambda") + ylab("waiting_time")

# From client (ia_conn)
# lambda = 0.01883835
# Thus mu = packets/second = 128000/100.5 = 1273.632 packets/second
# rho = 1.479105e-05
# N = 1.479127e-05
# W = 1.161345e-08
mu1 <- 1273.632
ggplot(mapping = aes(seq(0, mu1, 2), queue_size(seq(0, mu1, 2), mu1))) + geom_line() + xlab("lambda") + ylab("queue_size")
ggplot(mapping = aes(seq(0, mu1, 2), waiting_time(seq(0, mu1, 2), mu1))) + geom_line() + xlab("lambda") + ylab("waiting_time")

