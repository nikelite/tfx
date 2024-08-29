# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TFX orchestration.experimental module."""
try:
  from tfx.orchestration.kubeflow.v2 import kubeflow_v2_dag_runner  # pylint: disable=g-import-not-at-top

  KubeflowV2DagRunner = kubeflow_v2_dag_runner.KubeflowV2DagRunner
  KubeflowV2DagRunnerConfig = kubeflow_v2_dag_runner.KubeflowV2DagRunnerConfig
  del kubeflow_v2_dag_runner
except ImportError:  # Import will fail without kfp package.
  pass
