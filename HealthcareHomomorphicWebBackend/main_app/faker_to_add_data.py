from django.contrib.auth import get_user_model
from faker import Faker
from .models import *
import random

User = get_user_model()
fake = Faker()


def start():
        
    # create 10 user instances with fake email and phone numbers
    for i in range(10):
        user = User.objects.create(
            email=fake.email(),
            phone=fake.phone_number(),
        )

        # create corresponding TbPatientInfo and TbPatientReport instances for each user
        TbPatientInfo.objects.create(
            patient=user,
            gender=random.choice(['Male', 'Female']),
            heart_rate=random.uniform(60, 120),
            height=random.uniform(1.5, 2),
            mass=random.uniform(40, 100),
            sugar_level=random.uniform(4, 10),
            hb_level=random.uniform(100, 200),
            wbc_count=random.uniform(4, 12),
            residual_volume=random.uniform(1, 5),
            vital_capcity=random.uniform(2, 6),
            body_temp=random.uniform(36, 38),
        )

        TbPatientReport.objects.create(
            patient=user,
            bmi=random.uniform(18.5, 30),
            is_fever=fake.boolean(),
            total_lung_capacity=random.uniform(4, 8),
        )
