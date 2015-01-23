library(shiny)
library(rjson)

setwd('~/GitHub/MiningBalls')
firstRun = TRUE

# Details of each fixture including teams, score and date
match_data <- lapply(readLines('log.txt'), fromJSON)
match_IDs <- lapply(match_data, function(x) paste(x[['id']]))
names(match_IDs) <- lapply(match_data, function(x) paste(x['homeTeam'],'v',x['awayTeam']))

# Details of teams, including short names and logo image URLs
team_data <- fromJSON(file='teams.json')
team_names <- lapply(team_data, function(x) x[['name']])
team_hashtags <- fromJSON(file='team_hashtags.json')

# Has same indices as match_data
match_hashtags <- lapply(match_data, function(x) list(homeTag = team_hashtags[[x[['homeTeam']]]],
                                                      awayTag = team_hashtags[[x[['awayTeam']]]]))

shinyServer(function(input, output) {
  
  output$teams <- renderPrint({
    team_names
  })
  
  output$matchChooser <- renderUI({
    selectInput("chosen_match",
                h4("Football match"),
                match_IDs
                ) 
  })
  
#   ###
#   output$testtext <- renderPrint({
#     unlist(match_hashtags[input$chosen_match==match_IDs], recursive=FALSE)[input$chosen_tag]
#   })
#   ###
  
  output$tagChooser <- renderUI({
    selected_match <- input$chosen_match==match_IDs
    tag_choices = names(unlist(match_hashtags[selected_match],recursive=FALSE)) #homeTag, awayTag
    names(tag_choices) = unlist(match_hashtags[selected_match],recursive=FALSE)
    selectInput("chosen_tag",
                h4("Plot by hashtag"),
                tag_choices
                )
  })
  
  output$scoreboard <- renderText({
    selected <- input$chosen_match==match_IDs
    match <- unlist(match_data[selected], recursive=FALSE)
    paste(match$homeTeam, match$goalsHomeTeam,
          '-',
          match$goalsAwayTeam, match$awayTeam)    
  })
  
  output$sentimentPlot <- renderPlot({
    match_file <- paste0('tweets/', input$chosen_match, '.csv')
    if(!file.exists(match_file) && firstRun) tweets <- data.frame(time=seq(1,10,1), sentiment = 5*rnorm(10))
    else tweets <- read.csv(match_file)
    firstRun=FALSE
    tweets$time <- as.POSIXct(tweets$time, origin="1970-01-01")
    plot(tweets$time,
         lowess(tweets$time, f=input$f, tweets$sentiment)$y,
         col='limegreen', type='l', lwd=2,
         ylab='Tweet sentiment',
         main=input$matchChooser,
         xlab='Time')
    graphTag <- unlist(match_hashtags[input$chosen_match==match_IDs], recursive=FALSE)[input$chosen_tag]
    if (input$plotByTag){
      chosenTweets <- tweets[tweets$hashtags==graphTag,]
      lines(chosenTweets$time,
            lowess(chosenTweets$time, f=input$f, chosenTweets$sentiment)$y,
            col='blue', lty=3)
    }

    
#     if(length(input$hashTag)>0) {
#       for (k in input$hashTag) {
#         title(main=legendTags[k])
#         lines(lowess(tweets$time[tweets$hashtags=='EFC'],
#               tweets$sentiment[tweets$hashtags=='EFC']),
#               col=c(1,2,3,4,5)[k])
#       }
#       legend("bottomleft", legend=legendTags, lwd=2, col=c('red','blue'))
#     }
 })
})