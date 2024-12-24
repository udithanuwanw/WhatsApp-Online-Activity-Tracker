function startnew(){
    var online = {};
    var parentWindow ;
    
    window.Store.Presence.toArray().forEach(function(c) {
    if (!c || !c.id)
    return;
    
    if (!c.isSubscribed) {
    c.subscribe();
                    }
    if (!c.chatActive) {
    c.chatActive=true;
                    }	
    if (!c.hasData) {
    c.hasData=true;
                    }							
    
    
    if (c.isOnline == undefined)
    return;
    
    
    if (c.isOnline==true){
        console.log(c.id+ '');
        
    } 
    
        });		
            
        }		
    startnew();
                