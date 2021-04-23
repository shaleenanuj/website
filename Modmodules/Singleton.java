class Singleton
{
 private static single_instance = null ;
 
 
 private Singleton(int offset )
 {
  this.offset = offset; 
 
 }
  public static SingletonClass getInstance() {

        if (single_instance == null) {  

          synchronized(Singleton.class) {

          single_instance = new Singleton();
           
         
        
        }}
        
   public static dump_data()
   {
        single_
   
   
   
    /*  data = {}
			data['people'] = []  
			data['people'].append({  
    			'path': str(self.dirPath),
    			'image_prefix':str(self.filePrefix),
    			'offset': str(self.offset)
			 })
   
   */
   
   }
 
 	return single_instance;

 
 }
 } 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
/*
 
 public class SingletonClass {

    private static SingletonClass SINGLE_INSTANCE = null;

    private SingletonClass() {}

    public static SingletonClass getInstance() {

        if (SINGLE_INSTANCE == null) {  

          synchronized(SingletonClass.class) {

          SINGLE_INSTANCE = new SingletonClass();

          }

        }

        return SINGLE_INSTANCE;

    }

}


 
 
 */
 



