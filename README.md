# friendly-goggles
LLM chat app(CLI and very bare bones ofcourse) with Contextual Memory and Some chicky little resources regarding research papers

# Blog Time
So I was getting bored and someone in a group chat mentioned about making an LLM which mimics that human... hmmmmm.. so it seems like it is time to code something up. 
Now what they did was use GPT's API and their data from whatsapp to create a version of themselves which sounds like a good idea. But not good enough for us aha. So I sat down and thought hmmm what can be done to make something cool but simple enough. Brain twinkle-twinkled and what can I say, my brain can think (XD).

So the plan is simple, Make a CLI and very barebones application which has contextual memory (that is, it can remember what you guys were talking about from like 20 messages ago and probably after an year as well if you let the memory persist without deleting it, A good friend for ranting I suppose). Along with contextual memory, I think I'd like to add a way to upload research papers to it so that the LLM can talk with the knowledge of those papers (and probably be able to connect research paper if it has to).

Now each branch will be a feature which gets added along with some blogging cause why not, right? I just thought it would be a cool way to communicate my thoughts before I hopefully start working on making a youtube channel.


## Jul 18 02:22:36 AM
So I tried using LLaMA-cpp, which means that I was planning to run the model locally. We ain't no kids to use OpenAI's GPT API. But well cause I don't have a great CPU and GPU that plan kinda failed soon (we went from tokens per second to minutes per token real quick)
Now what? We shift to petals and try that out. What is petals you might ask? good thing you did, its a decentralized way of running LLMs. Check it out and maybe put your GPU there to make the whole thing faster?! :D
The model of choice was LLaMa-65B but I was getting a validation error for that lad so I switched to Bloom but might get a validation error again. Idk what the F is that time error which it keeps on throwing at me for no reason and it still has 5 mins remaining to download while I update this blog.


## Jul 18 03:07:38 AM
After spending almost an hour to figure out why was I getting the "ValidationError: local time must be less that 3 seconds than others" which didn't make sense at all. I fixed it by installing chrony and enabling ntp (for debian/ubuntu I think you can get away with using ntpdate but who am I to guess that, I use void anyways).

Well now we have the LLaMa-65B model working so lets go! thats progress.
![](img/2023-07-18-03-17-17.png) what?
