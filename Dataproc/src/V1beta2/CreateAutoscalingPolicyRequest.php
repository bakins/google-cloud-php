<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc/v1beta2/autoscaling_policies.proto

namespace Google\Cloud\Dataproc\V1beta2;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * A request to create an autoscaling policy.
 *
 * Generated from protobuf message <code>google.cloud.dataproc.v1beta2.CreateAutoscalingPolicyRequest</code>
 */
class CreateAutoscalingPolicyRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * Required. The "resource name" of the region, as described
     * in https://cloud.google.com/apis/design/resource_names of the form
     * `projects/{project_id}/regions/{region}`.
     *
     * Generated from protobuf field <code>string parent = 1;</code>
     */
    private $parent = '';
    /**
     * The autoscaling policy to create.
     *
     * Generated from protobuf field <code>.google.cloud.dataproc.v1beta2.AutoscalingPolicy policy = 2;</code>
     */
    private $policy = null;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type string $parent
     *           Required. The "resource name" of the region, as described
     *           in https://cloud.google.com/apis/design/resource_names of the form
     *           `projects/{project_id}/regions/{region}`.
     *     @type \Google\Cloud\Dataproc\V1beta2\AutoscalingPolicy $policy
     *           The autoscaling policy to create.
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Google\Cloud\Dataproc\V1Beta2\AutoscalingPolicies::initOnce();
        parent::__construct($data);
    }

    /**
     * Required. The "resource name" of the region, as described
     * in https://cloud.google.com/apis/design/resource_names of the form
     * `projects/{project_id}/regions/{region}`.
     *
     * Generated from protobuf field <code>string parent = 1;</code>
     * @return string
     */
    public function getParent()
    {
        return $this->parent;
    }

    /**
     * Required. The "resource name" of the region, as described
     * in https://cloud.google.com/apis/design/resource_names of the form
     * `projects/{project_id}/regions/{region}`.
     *
     * Generated from protobuf field <code>string parent = 1;</code>
     * @param string $var
     * @return $this
     */
    public function setParent($var)
    {
        GPBUtil::checkString($var, True);
        $this->parent = $var;

        return $this;
    }

    /**
     * The autoscaling policy to create.
     *
     * Generated from protobuf field <code>.google.cloud.dataproc.v1beta2.AutoscalingPolicy policy = 2;</code>
     * @return \Google\Cloud\Dataproc\V1beta2\AutoscalingPolicy
     */
    public function getPolicy()
    {
        return $this->policy;
    }

    /**
     * The autoscaling policy to create.
     *
     * Generated from protobuf field <code>.google.cloud.dataproc.v1beta2.AutoscalingPolicy policy = 2;</code>
     * @param \Google\Cloud\Dataproc\V1beta2\AutoscalingPolicy $var
     * @return $this
     */
    public function setPolicy($var)
    {
        GPBUtil::checkMessage($var, \Google\Cloud\Dataproc\V1beta2\AutoscalingPolicy::class);
        $this->policy = $var;

        return $this;
    }

}
