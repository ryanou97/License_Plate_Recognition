import cv2
import module as m     # 匯入自訂模組


if __name__ == '__main__':
    
    capture = cv2.VideoCapture(0)   # 建立攝影機物件
    
    
    if capture.isOpened():          # return True 為開啟成功  
        
        try:
            while True:
                sucess, img = capture.read()        # 讀取影像
                if sucess:
                    cv2.imshow('Frame', img)        # 顯示影像
               
            
    
                # 等待鍵盤輸入
                k = cv2.waitKey(100)                
                
                # 按下 'S' or 's' > 畫面儲存 > 進行車牌辨識
                if k == ord('s') or k == ord('S'):
                    cv2.imwrite('shot.jpg', img)    
                    text = m.get_license(img)         
                    print('車牌:', text)
                    
                # 按下 'Q' or 'q' > 關閉畫面、攝影機 > break
                if k == ord('q') or k == ord('Q'): 
                    print('結束辨識')
                    cv2.destroyAllWindows()   
                    capture.release()       
                    break
        except:
            print("功能出錯")
    
    else:
        
        print('開啟攝影機失敗')

 



