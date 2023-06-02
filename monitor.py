import configparser
import json
from youtube_transcript_api import NoTranscriptFound

from yt_search import  get_latest_video_id, get_transcript
import openai_client
import check_config
from bot import use_bots
from utils import log_and_send

main_config = configparser.ConfigParser()
main_config.read("./configs/mainconf.ini")

transcript = """
we're gonna feed big ounce this entire shark oh no jellyfishing look how good he is at flying now and this is actually in the tutorial for RuneScape okay guys time to cook big gowns good morning everybody listen to the cars driving by my home this is my son Patrick Bateman he hasn't eaten since last night and look at this master Oogway sleeps with him in here it's the cutest thing ever I'm giving this boy his bottle of the morning my friend Pierce will be taking care of him for the rest of the day and all the other animals this guy only takes nine to ten ounces twice a day now which is awesome we're weaning him slowly next week he's gonna only take eight to nine ounces but for now this boy is eating a ton of grass he's eating a lot of this stuff precious lit hope hap Twix but he kills his bottles still we got a big rain last night and me my buddy are going to be going to the coast to get on some sharks we're going to meet with B alt and Kyle the fish Whisperer also look he poops the little pellets now I'm bringing my sons you bring a bones because he's a teenager now and it's time he learns how to catch a shark all right everybody I'm gonna make sure that we have some kerosene for the fire because we're going to be camping on the beach in Texas again everything's nice and ready here for the game wardens inspection and my buddy brought me some new pigeons from his buddy's old flock and one of them is brown about to just go full Mike Tyson start pigeon breeding I don't even care my pigeon collection will be much more robust than Mike Tyson's in the ah look at these fruit trees you guys I haven't even planted them and there's already some nice fruit on them I might just pick this delicious but the Cappies are all doing okay petunia always loves the rain and even the baby and his wife didn't mind the rain last night look how precious this little girl is also she's really friendly she lets me get super close to her now but this is the part I'm the most excited to show you guys today look at this the Gosling babies are thriving and they have this whole little area to grow up and play look how precious they are you guys and they just follow her around all day oh I hear tree frog do you hear that baby there's a tree frog over there every time after a big rain here in Texas and back in Pennsylvania you'll hear all the tree frogs in the trees and they're letting each other know tonight's the night we find a wife boys and we even have a native sunflower grown over there look at all right guys that's it I'm gonna clean everything up here give these guys their food to make things a little easier for Pierce I'm sick of this I'm sick of homelander being so dang cute I'm sick of Kevin attacking me and being crinned every time I try to give him a little pet he just tries to go oh look he's getting the sumies look how precious this little man is oh I'm sick of this I'm going to Matagorda to Texas right now the baby moment goodbye to baby be safe while I'm gone precious little man all right get over here did you think you could slap me in the face and scratch me he did and it hurt real bad oh no no no no no don't pick my plum no it's not it's clearly not right look at it but they are pretty good for being the boys wow they're actually eating them how about y'all go in the comments and say wow Uncle Ben can't wait for this epic anime Beach episode oh here we are on the beach oh that's right everyone in Texas you're allowed to just drive on the beach if you get a beach pass but you gotta have four-wheel drive I'm gonna crash so I pulled up and I saw Kyle the fish Whisperer and this nice stranger catching shrimp in a net and because I caught thousands of shrimp on RuneScape I figured how hard could it be sweet check this out you guys it's a little baby look down I think that's a look down that is so cool put this boy right back in the ocean these shrimp are mine and all we needed was a cast net for these it's a little baby sea trap got one little tooth on his front face what is this tiny fish oh sweet Wampum oh look how cute he is Pelican moment this is geronimo's first shark he caught this all by himself thanks to Kyle's dogless hooks the hook came right out come on like the gar we have in our pond now that Kyle tagged this sharks we're gonna be able to track how does that work Kyle the waves were a little too loud to hear but because of the fish tagging we can track how fast they're growing and where they're migrating okay this one because it's tagged we're going to go ahead and release it but the next one we catch is going to be food for big owls Jabron gabon's first trip to the beach wow he caught that all by himself oh elegant moment but for the rest of this day this little Fella's just hanging out here he's still too young to just straight up fly away but I still need to keep an eye on them because these Pelicans could eat them and that's not even a joke there's tons of videos of this oh no look at this beautiful strong man I'm just gonna keep all the shrimp that I'm catching so I can feed big ounce tonight also we have no food we didn't bring any food we're just look guys I caught this little catfish I'm gonna release him though amazing that we have catfish here in the ocean dinner look guys I caught a little baby Jack jellyfishing jelly fishing jellyfishing do we worship it delicious here let me see slippery oh my God careful take this it's dangerous out there it might fall it might fall off you think we can drink out of this okay listen guys when I said that I was in a little bit of a silly goofy mood I didn't think he would actually fill it up with seawater and try and drink it but can someone in the comments please explain why this actually stung him how bad is it can I get a look it's like it's like that sucks throw us your tongue show us your tongue thank you whoa look at this guys I totally fairhooked this truck look at this guys I got this five pound bluegill without using any means of bear of foul hooking at all say what you will snowflakes but Uncle Ben's going pescetarian now actually you know what anything you can do in Minecraft or RuneScape I'm gonna do in real life for you guys and this is actually in the tutorial for RuneScape and big ounce caught all of these by himself trip moment trip moment above average for sure and we're gonna season them throw them on fire sounds like a lot of work to me I'm gonna play fortnite cringe very cringe not as cool as mine please go thank Kyle the fish Whisperer for making this amazing shrimp cocktail it's a golden brown color delicious oh sweet one bigger tint is not a good Tent Maker we lost big ounce he's gone oh look at he's going under the walk okay guys time to cook big ounce look big ounce we cooked you some shrimp let's just go ahead and put you right on the Cove just kidding I'm gonna go ahead and put him back in the tent so he stays away from the mosquitoes because we don't want him getting West Nile Virus and the best thing about shark fishing you guys that you can catch them during the day or at night got this all by myself without any help from anyone at all I caught this all by myself whoa is that the one we tagged earlier oh be careful bro be careful and that's a barbless hook so we can take that right out of there and that sure is a nice bluegill big ounce wake up we got a shark buddy come on buddy let's go we got a shark the fella was just sleeping in here come on big humps we got a shark wake up wow what do you think big ounce it's a shark gonna feed big ounce this entire shark okay now that Kyle tagged it we're gonna be putting it back but we're gonna let big ounce take one little bite there you go buddy wow big ounce touched a shot and be all it's gonna let this little fella go right back into the abyss bounce Ketchum there's a show hey it's me big Alps thanks so much Dad for taking me on this epic shark fishing trip I sure do love you appreciate you goodbye okay big ounce I'm sorry for waking you up I'll put you back good night bibber 10. look how precious he is thanks for inviting me out on this shark fishing trip oh is that a shark don't mind if I do I'm in my underwear get back here little boy get back here check this out you guys when I use my Spotlight look at this whoa look at all those mullets look at that a delectable morsel precious little fella all right everybody it's time for bed I'm in my tent slow fella and I will be cuddling tonight it's warm enough to where I don't really need a sleeping bag I literally am just sleeping in this cringe uh tent with a pigeon honestly you guys even though this is a little weird just really thankful that I get the chance to do this because if I thought this little man was gonna die remember literally a couple months ago when we thought this man was gonna die for sure thankfully the good Lord protect him and kept him alive I love you guys I appreciate you and I'll see you tomorrow morning okay so we packed all this stuff up to move Kyle and Grandma let these guys get their morning Zoomies out your Brenda bows first beach trip he still has those little chick feathers precious no big ounce don't eat the sand watch this you guys look how good he is at flying now oh take the graham cracker bigger tits wow take your turn at the beach eating a graham cracker okay time to pack these boys up and move them over to the next spot get in there to bringle bones get in there come on precious little baby oh next thing you know we hooked into another large ocean creature hi old fish Whisperer this is the southern Stingray I can lift it I actually can grab the leader if you want when is a stingray ever hurt someone before oh you're not thinking about stabbing me with that ball okay guys I'm gonna lip it no no we need to get big ounce first wake up we have to go eat a stingray this will be big ounces first ever Stingray big house is enamored with the Majesty of creation entire Stingray and one bite today Mr ounce actually Avenged Stever okay big ounce go have fun in the woods over there goodbye bingerton one two buckle my shoe wow guys wasn't that a great fishing trip we sure learned a lot about fishing friendship and Jellyfish also big ounces dead but I love you guys I appreciate you thanks so much for watching my video the game warden did just pass our inspection for wildlife rehab so now we can finally start rescuing all the wild animals in Texas I love you guys I appreciate you thanks so much for watching my videos and we'll see you in the next video oh almost forgot to tell you
"""

def get_stored_video_id():
    try:
        with open('latest_video.json', 'r') as file:
            data = json.load(file)
            return data.get('latest_video_id')
    except Exception as e:
        log_and_send("Failed to get stored video ID:", e, "error")
        
def store_video_id(video_id):
    try:
        with open('latest_video.json', 'w') as file:
            json.dump({'latest_video_id': video_id}, file)
    except Exception as e:
        log_and_send("Failed to store video ID:", e, "error")

def new_video(video_id):
    log_and_send("Attempting to summarize new video and use bots...")
    #transcript, error = get_transcript(video_id)
    transcript = "This is a test transcript right now. Bombtza?!??!?! Also talk about palm trees."
    #error = NoTranscriptFound(None,None,None)
    error = None
    if error is not None:
        if type(error) is NoTranscriptFound:
            log_and_send("get_transcript() returned NoTranscriptFound. Will retry in the next run.", level="warning")
            store_video_id("") # makes the video appear new again for another try
    else:
        try:
            openai_response = openai_client.api_call(main_config, transcript)
            summarized = openai_response["choices"][0]["text"]
            use_bots(main_config, summarized)
            log_and_send("Summarized and and used bots..")
        except Exception as e:
            log_and_send("Failed to summarize and post new video: ", e, "error")
  
def main():
    
    check_config.check(main_config)
    
    log_and_send("Config setup correctly. Starting now.")
    
    try:
        latest_video_id = get_latest_video_id(main_config, channel_id=main_config.get("YOUTUBE", "CHANNEL_ID"), channel_name=main_config.get("YOUTUBE", "CHANNEL_NAME"))
        stored_video_id = get_stored_video_id()

        if latest_video_id != stored_video_id:
            store_video_id(latest_video_id)
            log_and_send("New video uploaded. Stored new video ID: " + latest_video_id)
            new_video(latest_video_id)
        else:
            log_and_send("No new video uploaded. Stopped.")

    except Exception as e:
        log_and_send("An error occurred in main", e, "error")
    
if __name__ == "__main__":
    main()
