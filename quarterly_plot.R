library(ggfortify)

setwd("~/Downloads/550project")

training_ave <- read.csv("Training_Average_Price.csv", header = FALSE)
df <- t(training_ave)
df <- as.data.frame(df, stringsAsFactors=FALSE)
df$V1[1] <- "Date"
names(df) <- df[c(1),]
df <- df[-c(1),]
rownames(df) <- df[,1]
table <- df[,-c(1)]

quarter_table <- table[c(3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84),]
time <- c("2012.7","2012.10","2013.1","2013.4","2013.7","2013.10","2014.1","2014.4","2014.7","2014.10","2015.1","2015.4","2015.7","2015.10","2016.1","2016.4","2016.7","2016.10","2017.1","2017.4","2017.7","2017.10","2018.1","2018.4","2018.7","2018.10","2019.1","2019.4")
rownames(quarter_table) <- time


area_91107_q <- as.numeric(quarter_table$`91107`)
area_91775_q <- as.numeric(quarter_table$`91775`)
area_91006_q <- as.numeric(quarter_table$`91006`)
area_91024_q <- as.numeric(quarter_table$`91024`)
area_91016_q <- as.numeric(quarter_table$`91016`)
area_91706_q <- as.numeric(quarter_table$`91706`)
area_91010_q <- as.numeric(quarter_table$`91010`)
area_91702_q <- as.numeric(quarter_table$`91702`)
area_91722_q <- as.numeric(quarter_table$`91722`)
area_91741_q <- as.numeric(quarter_table$`91741`)
area_91740_q <- as.numeric(quarter_table$`91740`)

data_input_all <- autoplot(ts( cbind(area_91107_q,area_91775_q,
                                     area_91006_q,area_91024_q,area_91016_q,
                                     area_91706_q,area_91010_q,area_91702_q,
                                     area_91722_q,area_91741_q,area_91740_q)  , start = c(2012,7), frequency = 4 ),
                           facets = FALSE, xlab = "Time", ylab = "Ave_Price",
                           title = "Ave_Price_Quarter", axis.text.x = TRUE)
ggplotly(p = data_input_all)


