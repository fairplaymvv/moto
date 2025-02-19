import logging

import boto3
import sure  # noqa # pylint: disable=unused-import

from moto import mock_ec2

logger = logging.getLogger(__name__)


@mock_ec2
def test_disable_ebs_encryption_by_default():
    ec2 = boto3.client("ec2", "eu-central-1")

    ec2.enable_ebs_encryption_by_default()
    response = ec2.get_ebs_encryption_by_default()
    response.should.have.key("EbsEncryptionByDefault").equal(True)

    ec2.disable_ebs_encryption_by_default()
    after_disable_response = ec2.get_ebs_encryption_by_default()
    after_disable_response.should.have.key("EbsEncryptionByDefault").equal(False)


@mock_ec2
def test_enable_ebs_encryption_by_default():
    ec2 = boto3.client("ec2", region_name="eu-central-1")
    response = ec2.enable_ebs_encryption_by_default()

    ec2.get_ebs_encryption_by_default()
    response.should.have.key("EbsEncryptionByDefault").equal(True)


@mock_ec2
def test_get_ebs_encryption_by_default():
    ec2 = boto3.client("ec2", region_name="eu-west-1")

    response = ec2.get_ebs_encryption_by_default()
    response.should.have.key("EbsEncryptionByDefault").equal(False)


@mock_ec2
def test_enable_ebs_encryption_by_default_region():
    ec2_eu = boto3.client("ec2", region_name="eu-central-1")
    ec2_eu.enable_ebs_encryption_by_default()

    response = ec2_eu.get_ebs_encryption_by_default()
    response.should.have.key("EbsEncryptionByDefault").equal(True)

    ec2_us = boto3.client("ec2", region_name="us-east-1")
    response = ec2_us.get_ebs_encryption_by_default()
    response.should.have.key("EbsEncryptionByDefault").equal(False)
