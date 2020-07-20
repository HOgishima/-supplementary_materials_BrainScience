library(rstan)
options(mc.cores = parallel::detectCores())
rstan_options(auto_write = TRUE)

# import data
## 
df <- read.csv('XXXXXXX.csv',stringsAsFactors = F, header = T)

# make dataset
data <- list(T=nrow(df),
             N=nlevels(factor(df$subject)),
             Tsubj=40,
             choice=df$choice,
             outcome=df$outcome)

fit <- stan(file='./rl_model.stan',data=data,seed=1234,control=list(adapt_delta=0.99),chains = 4)#,iter=1000,warmup=500)

# result
summary(fit)
write.csv(summary(fit), "./result.csv")
