# value = 99
# def prime(value):
#     for i in range(2,(value//2)+1):
#         if value%i == 0:
#             return print('not prime')

#     return print('prime')
# prime(value)
# first = 0
# second = 1
# a = 10
# for i in range(a+1):
#     print(first,end=' ')
#     third = first + second
#     first = second
#     second = third

# a = 'chikyzzzzzza'
# b = 0
# u = input('enter char')
# for i in a:
#     if u == i :
#         b +=1
# print(b,u,sep=':')


# l = [{'country':'india','capital':'delhi'},{'country':'afganistan','capital':'kabul'}]

# l[0]['capital'],l[1]['capital']=l[1]['capital'],l[0]['capital']
# # l[1]['capital']=a
# print(l)
import cv2
import os

list_of_names = [('Aayushmaan Aayushmaan','python Workshop')]
output_directory = "C:\\Users\\acer\\Desktop\\python\\p_i_s"

# Check if the output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def generate_certificates():
    for index, name in enumerate(list_of_names):
       
        certificate_template_image = cv2.imread("C:\\Users\\acer\\Desktop\\python\\p_i_s\\certificate-template.jpg")
        
        # Calculate the position dynamically based on the length of the name
        text_size, _ = cv2.getTextSize(name[0].strip(), cv2.FONT_HERSHEY_SIMPLEX, 3, 5)
        text_width = text_size[0]
        text_height = text_size[1]
        position_x = (certificate_template_image.shape[1] - text_width-50) // 2  # Center horizontally
        position_y = (certificate_template_image.shape[0] + text_height+200) // 2  # Center vertically
        
        cv2.putText(certificate_template_image, name[0].strip(), (position_x, position_y), cv2.FONT_HERSHEY_TRIPLEX, 3, (8,8,8),2, cv2.LINE_AA)
        cv2.putText(certificate_template_image, name[1].strip(), (1360, 1151), cv2.FONT_HERSHEY_TRIPLEX, 2, (8,8,8),2, cv2.LINE_AA)
        cv2.imwrite(os.path.join(output_directory, "{}.jpg".format(name[0].strip())), certificate_template_image)
        print("Processing {} / {}".format(index + 1, len(list_of_names)))

generate_certificates()
