provider "aws" {

region = "us-east-1"
profile = "default"
}

# Step 1

resource "aws_instance"  "Amazon" {
ami = "ami-0d5eff06f840b45e9"
instance_type = "t2.micro"
key_name = "Key"
tags = { Name : "Terraform_1_Amazon" }
}

output "Public_IP" {
 value = aws_instance.Amazon.public_ip
}

output "Availability_Zone" {
 value = aws_instance.Amazon.availability_zone
}

# Step 2
resource "aws_ebs_volume" "Extra_Storage" {
 availability_zone = aws_instance.Amazon.availability_zone
 size = 5
 tags = {
  Name = "Adarsh New HD"
 }
}


output "Storage" {
 value = aws_ebs_volume.Extra_Storage.id
}

# Step 3
resource "aws_volume_attachment" "EBS_Attachment"{
 device_name = "/dev/sdh"
 volume_id = aws_ebs_volume.Extra_Storage.id
 instance_id = aws_instance.Amazon.id
}

output "Result" {
 value = aws_volume_attachment.EBS_Attachment
}
