# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-rapidfuzz
Epoch: 100
Version: 3.9.6
Release: 1%{?dist}
Summary: Rapid fuzzy string matching
License: MIT
URL: https://github.com/rapidfuzz/rapidfuzz/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cmake
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-scikit-build >= 0.16.2
BuildRequires: python3-setuptools >= 42.0.0

%description
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rapidfuzz
Summary: Rapid fuzzy string matching
Requires: python3
Provides: python3-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python3dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rapidfuzz) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-rapidfuzz
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.

%files -n python%{python3_version_nodots}-rapidfuzz
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-rapidfuzz
Summary: Rapid fuzzy string matching
Requires: python3
Provides: python3-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python3dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rapidfuzz) = %{epoch}:%{version}-%{release}

%description -n python3-rapidfuzz
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.

%files -n python3-rapidfuzz
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-rapidfuzz
Summary: Rapid fuzzy string matching
Requires: python3
Provides: python3-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python3dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rapidfuzz) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rapidfuzz = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rapidfuzz) = %{epoch}:%{version}-%{release}

%description -n python3-rapidfuzz
RapidFuzz is a fast string matching library for Python and C++, which is
using the string similarity calculations from FuzzyWuzzy.

%files -n python3-rapidfuzz
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
