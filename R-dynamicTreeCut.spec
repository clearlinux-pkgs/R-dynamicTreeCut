#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dynamicTreeCut
Version  : 1.63.1
Release  : 6
URL      : https://cran.r-project.org/src/contrib/dynamicTreeCut_1.63-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dynamicTreeCut_1.63-1.tar.gz
Summary  : Methods for Detection of Clusters in Hierarchical Clustering
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n dynamicTreeCut
cd %{_builddir}/dynamicTreeCut

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589516522

%install
export SOURCE_DATE_EPOCH=1589516522
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynamicTreeCut
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynamicTreeCut
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dynamicTreeCut
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dynamicTreeCut || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dynamicTreeCut/DESCRIPTION
/usr/lib64/R/library/dynamicTreeCut/INDEX
/usr/lib64/R/library/dynamicTreeCut/Meta/Rd.rds
/usr/lib64/R/library/dynamicTreeCut/Meta/features.rds
/usr/lib64/R/library/dynamicTreeCut/Meta/hsearch.rds
/usr/lib64/R/library/dynamicTreeCut/Meta/links.rds
/usr/lib64/R/library/dynamicTreeCut/Meta/nsInfo.rds
/usr/lib64/R/library/dynamicTreeCut/Meta/package.rds
/usr/lib64/R/library/dynamicTreeCut/NAMESPACE
/usr/lib64/R/library/dynamicTreeCut/R/dynamicTreeCut
/usr/lib64/R/library/dynamicTreeCut/R/dynamicTreeCut.rdb
/usr/lib64/R/library/dynamicTreeCut/R/dynamicTreeCut.rdx
/usr/lib64/R/library/dynamicTreeCut/help/AnIndex
/usr/lib64/R/library/dynamicTreeCut/help/aliases.rds
/usr/lib64/R/library/dynamicTreeCut/help/dynamicTreeCut.rdb
/usr/lib64/R/library/dynamicTreeCut/help/dynamicTreeCut.rdx
/usr/lib64/R/library/dynamicTreeCut/help/paths.rds
/usr/lib64/R/library/dynamicTreeCut/html/00Index.html
/usr/lib64/R/library/dynamicTreeCut/html/R.css
