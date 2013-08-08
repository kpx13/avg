jQuery.fn.suSlider = function(options){
	
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Declare variables and functions
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	var defaults = {
		mode: 'slide',
		speed: 500,
		auto: false, 
		pause: 3000,
		select:10000,
		width: $(this).children('.silderitem').width(), 
		wrapper_class: 'container'
	}; 
	options = $.extend(defaults, options); 
	var $this = $(this);

	var $parent_width = options.width; 
	var is_working = false;
	var child_count = $this.children('.silderitem').size(); 
    var idx=0;		
	var isbreak=false; 
	var expauuse=0;
	var gotoidx=-1;
	var hoverhold=false;
		function animate_idx(i){
		
		is_working = true; 
		$this.animate({'left':'-' + $parent_width * i + 'px'}, options.speed, function(){ 
			idx=i;
			is_working = false; 
	   		$('#slnav li:.active').removeClass('active');
			$('#slnav li:eq('+idx+')').addClass('active');
        if(options.auto && !isbreak)
          { 
           
            idx++;
           if(idx==child_count)
            {
                idx=0;
            }
             clearInterval($.t);
	         $.t = setInterval(function(){animate_idx(idx);}, expauuse==0 ? options.pause : expauuse);
	         expauuse=0;
           }
		});		
		
	}
	
	 
	 function fade_idx(idx){  
		    is_working = true; 
			$this.children('.silderitem').eq(idx).fadeTo(options.speed, 0, function(){$(this).hide();});
			if(gotoidx<0)
			{
            idx++;
             if(idx==child_count)
             {
                idx=0;
             }
            }
            else
            {
              idx=gotoidx;
            }
            gotoidx=-1;
            $('#slnav li:.active').removeClass('active');
			$('#slnav li:eq('+idx+')').addClass('active');
			$this.children('.silderitem').eq(idx).show().fadeTo(options.speed, 1, function(){
				
			is_working = false; 
			
			 
        if(options.auto && !isbreak)
          { 
         
             clearInterval($.t);
	         $.t = setInterval(function(){fade_idx(idx);}, expauuse==0 ? options.pause : expauuse);
	         expauuse=0;
           }
           
		}); 
	}
	 
	function add_controls(){  
	
	     $('#slnav').children().click(function(){		
			
			var $kids = $('#slnav li').index(this);
			clearInterval($.t);
			if(!is_working){
			
			    if(options.select==0)
				    {
				     isbreak=true;
				    }
				    else
				    { 
				      expauuse = options.select;
				    }
				
				if(options.mode == 'slide'){
										 
					animate_idx($kids); 
				    
				}  
				else
				{
				   var $on= $('#slnav li').index($('#slnav li:.active'));
				  gotoidx=$kids;
				  fade_idx($on);
				}
			}
								
			return false;
					
		});	
		 
	}
	
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// Create content wrapper and set CSS
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	$this.wrap('<div class="' + options.wrapper_class + '"></div>');
	 
			
	if(options.mode == 'slide'){
		
		$this.parent().css({
			'overflow' : 'hidden',
			'position' : 'relative',
			'width' : options.width + 'px'
		});
			
		$this.css({		
			'width' : '999999px',
			'position' : 'relative' 			 	
		});
			
		$this.children('.silderitem').css({		
			'float' : 'left',
			'width' : $parent_width
		});
		 	
		 
	
	}else if(options.mode == 'fade'){
		
		$this.parent().css({
			'overflow' : 'hidden',
			'position' : 'relative',
			'width' : options.width + 'px' 
		});
		 
		$this.children('.silderitem').css({		
			'position' : 'absolute',
			'width' : $parent_width,
			'listStyle' : 'none',
			'opacity' : 0,
			'display' : 'none'	
		});
		
		 $this.children('.silderitem:first').css({
			'opacity' : 1,
			'display' : 'block'
		}); 
				
	}
	
   add_controls();
   
   if(options.auto)
   { 
     
     clearInterval($.t);
     if(options.mode == 'slide'){
      $this.animate({'left':'-0px'}, options.speed, function(){ 
	 $.t = setInterval(function(){animate_idx(1);},options.speed);
	  });
	 }
	 else
	 {
	    
	      $.t =setInterval(function(){fade_idx(0);},options.speed*2);
	    
	 }
	 
   }
		
}