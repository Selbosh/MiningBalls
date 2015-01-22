library(shiny)
library(rjson)

saved_matches <- lapply(readLines('~/GitHub/MiningBalls/log.txt'), fromJSON)
match_names <- lapply(saved_matches, function(x) paste(x['homeTeam'],'v',x['awayTeam'])) 

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel('MineBalls'),
  h3('Twitter sentiment analyser'),
  
  # Sidebar with a dropdown to select match, and entry box for bandwidth
  sidebarLayout(
    sidebarPanel(
      selectInput(inputId = 'match',
                  label = 'Select match',
                  match_names,
                  selected=match_names[1]),
      numericInput('f',
                   'Scale:',
                   value = 1)
      ),    
    # Show a plot of the generated distribution
    mainPanel (
      h3(textOutput("scoreboard"), style='text-align:center;'),
      
      plotOutput('sentimentPlot')
      )
    )
  ))