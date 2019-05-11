/* File: wrapmodule.c
 * This file is auto-generated with f2py (version:2_1330).
 * Hand edited by Pearu.
 * f2py is a Fortran to Python Interface Generator (FPIG), Second Edition,
 * written by Pearu Peterson <pearu@cens.ioc.ee>.
 * See http://cens.ioc.ee/projects/f2py2e/
 * Generation date: Fri Oct 21 22:41:12 2005
 * $Revision:$
 * $Date:$
 * Do not edit this file directly unless you know what you are doing!!!
 */
#ifdef __cplusplus
extern "C" {
#endif

/*********************** See f2py2e/cfuncs.py: includes ***********************/
#include "Python.h"
#include "fortranobject.h"
#include <math.h>

static PyObject *wrap_error;
static PyObject *wrap_module;

/************************************ call ************************************/
static char doc_f2py_rout_wrap_call[] = "\
Function signature:\n\
  arr = call(type_num,dims,intent,obj)\n\
Required arguments:\n"
"  type_num : input int\n"
"  dims : input int-sequence\n"
"  intent : input int\n"
"  obj : input python object\n"
"Return objects:\n"
"  arr : array";
static PyObject *f2py_rout_wrap_call(PyObject *capi_self,
				     PyObject *capi_args) {
  PyObject * volatile capi_buildvalue = NULL;
  int type_num = 0;
  npy_intp *dims = NULL;
  PyObject *dims_capi = Py_None;
  int rank = 0;
  int intent = 0;
  PyArrayObject *capi_arr_tmp = NULL;
  PyObject *arr_capi = Py_None;
  int i;

  if (!PyArg_ParseTuple(capi_args,"iOiO|:wrap.call",\
			&type_num,&dims_capi,&intent,&arr_capi))
    return NULL;
  rank = PySequence_Length(dims_capi);
  dims = malloc(rank*sizeof(npy_intp));
  for (i=0;i<rank;++i)
    dims[i] = (npy_intp)PyInt_AsLong(PySequence_GetItem(dims_capi,i));

  capi_arr_tmp = array_from_pyobj(type_num,dims,rank,intent|F2PY_INTENT_OUT,arr_capi);
  if (capi_arr_tmp == NULL) {
    free(dims);
    return NULL;
  }
  capi_buildvalue = Py_BuildValue("N",capi_arr_tmp);
  free(dims);
  return capi_buildvalue;
}

static char doc_f2py_rout_wrap_attrs[] = "\
Function signature:\n\
  arr = array_attrs(arr)\n\
Required arguments:\n"
"  arr : input array object\n"
"Return objects:\n"
"  data : data address in hex\n"
"  nd : int\n"
"  dimensions : tuple\n"
"  strides : tuple\n"
"  base : python object\n"
"  (kind,type,type_num,elsize,alignment) : 4-tuple\n"
"  flags : int\n"
"  itemsize : int\n"
;
static PyObject *f2py_rout_wrap_attrs(PyObject *capi_self,
				      PyObject *capi_args) {
  PyObject *arr_capi = Py_None;
  PyArrayObject *arr = NULL;
  PyObject *dimensions = NULL;
  PyObject *strides = NULL;
  char s[100];
  int i;
  memset(s,0,100*sizeof(char));
  if (!PyArg_ParseTuple(capi_args,"O!|:wrap.attrs",
			&PyArray_Type,&arr_capi))
    return NULL;
  arr = (PyArrayObject *)arr_capi;
  sprintf(s,"%p",PyArray_DATA(arr));
  dimensions = PyTuple_New(PyArray_NDIM(arr));
  strides = PyTuple_New(PyArray_NDIM(arr));
  for (i=0;i<PyArray_NDIM(arr);++i) {
    PyTuple_SetItem(dimensions,i,PyInt_FromLong(PyArray_DIM(arr,i)));
    PyTuple_SetItem(strides,i,PyInt_FromLong(PyArray_STRIDE(arr,i)));
  }
  return Py_BuildValue("siOOO(cciii)ii",s,PyArray_NDIM(arr),
		       dimensions,strides,
		       (PyArray_BASE(arr)==NULL?Py_None:PyArray_BASE(arr)),
		       PyArray_DESCR(arr)->kind,
		       PyArray_DESCR(arr)->type,
		       PyArray_TYPE(arr),
		       PyArray_ITEMSIZE(arr),
		       PyArray_DESCR(arr)->alignment,
		       PyArray_FLAGS(arr),
		       PyArray_ITEMSIZE(arr));
}

static PyMethodDef f2py_module_methods[] = {

  {"call",f2py_rout_wrap_call,METH_VARARGS,doc_f2py_rout_wrap_call},
  {"array_attrs",f2py_rout_wrap_attrs,METH_VARARGS,doc_f2py_rout_wrap_attrs},
  {NULL,NULL}
};

#if PY_VERSION_HEX >= 0x03000000
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "test_array_from_pyobj_ext",
    NULL,
    -1,
    f2py_module_methods,
    NULL,
    NULL,
    NULL,
    NULL
};
#endif

#if PY_VERSION_HEX >= 0x03000000
#define RETVAL m
PyMODINIT_FUNC PyInit_test_array_from_pyobj_ext(void) {
#else
#define RETVAL
PyMODINIT_FUNC inittest_array_from_pyobj_ext(void) {
#endif
  PyObject *m,*d, *s;
#if PY_VERSION_HEX >= 0x03000000
  m = wrap_module = PyModule_Create(&moduledef);
#else
  m = wrap_module = Py_InitModule("test_array_from_pyobj_ext", f2py_module_methods);
#endif
  Py_TYPE(&PyFortran_Type) = &PyType_Type;
  import_array();
  if (PyErr_Occurred())
    Py_FatalError("can't initialize module wrap (failed to import numpy)");
  d = PyModule_GetDict(m);
  s = PyString_FromString("This module 'wrap' is auto-generated with f2py (version:2_1330).\nFunctions:\n"
"  arr = call(type_num,dims,intent,obj)\n"
".");
  PyDict_SetItemString(d, "__doc__", s);
  wrap_error = PyErr_NewException ("wrap.error", NULL, NULL);
  Py_DECREF(s);
  PyDict_SetItemString(d, "F2PY_INTENT_IN", PyInt_FromLong(F2PY_INTENT_IN));
  PyDict_SetItemString(d, "F2PY_INTENT_INOUT", PyInt_FromLong(F2PY_INTENT_INOUT));
  PyDict_SetItemString(d, "F2PY_INTENT_OUT", PyInt_FromLong(F2PY_INTENT_OUT));
  PyDict_SetItemString(d, "F2PY_INTENT_HIDE", PyInt_FromLong(F2PY_INTENT_HIDE));
  PyDict_SetItemString(d, "F2PY_INTENT_CACHE", PyInt_FromLong(F2PY_INTENT_CACHE));
  PyDict_SetItemString(d, "F2PY_INTENT_COPY", PyInt_FromLong(F2PY_INTENT_COPY));
  PyDict_SetItemString(d, "F2PY_INTENT_C", PyInt_FromLong(F2PY_INTENT_C));
  PyDict_SetItemString(d, "F2PY_OPTIONAL", PyInt_FromLong(F2PY_OPTIONAL));
  PyDict_SetItemString(d, "F2PY_INTENT_INPLACE", PyInt_FromLong(F2PY_INTENT_INPLACE));
  PyDict_SetItemString(d, "NPY_BOOL", PyInt_FromLong(NPY_BOOL));
  PyDict_SetItemString(d, "NPY_BYTE", PyInt_FromLong(NPY_BYTE));
  PyDict_SetItemString(d, "NPY_UBYTE", PyInt_FromLong(NPY_UBYTE));
  PyDict_SetItemString(d, "NPY_SHORT", PyInt_FromLong(NPY_SHORT));
  PyDict_SetItemString(d, "NPY_USHORT", PyInt_FromLong(NPY_USHORT));
  PyDict_SetItemString(d, "NPY_INT", PyInt_FromLong(NPY_INT));
  PyDict_SetItemString(d, "NPY_UINT", PyInt_FromLong(NPY_UINT));
  PyDict_SetItemString(d, "NPY_INTP", PyInt_FromLong(NPY_INTP));
  PyDict_SetItemString(d, "NPY_UINTP", PyInt_FromLong(NPY_UINTP));
  PyDict_SetItemString(d, "NPY_LONG", PyInt_FromLong(NPY_LONG));
  PyDict_SetItemString(d, "NPY_ULONG", PyInt_FromLong(NPY_ULONG));
  PyDict_SetItemString(d, "NPY_LONGLONG", PyInt_FromLong(NPY_LONGLONG));
  PyDict_SetItemString(d, "NPY_ULONGLONG", PyInt_FromLong(NPY_ULONGLONG));
  PyDict_SetItemString(d, "NPY_FLOAT", PyInt_FromLong(NPY_FLOAT));
  PyDict_SetItemString(d, "NPY_DOUBLE", PyInt_FromLong(NPY_DOUBLE));
  PyDict_SetItemString(d, "NPY_LONGDOUBLE", PyInt_FromLong(NPY_LONGDOUBLE));
  PyDict_SetItemString(d, "NPY_CFLOAT", PyInt_FromLong(NPY_CFLOAT));
  PyDict_SetItemString(d, "NPY_CDOUBLE", PyInt_FromLong(NPY_CDOUBLE));
  PyDict_SetItemString(d, "NPY_CLONGDOUBLE", PyInt_FromLong(NPY_CLONGDOUBLE));
  PyDict_SetItemString(d, "NPY_OBJECT", PyInt_FromLong(NPY_OBJECT));
  PyDict_SetItemString(d, "NPY_STRING", PyInt_FromLong(NPY_STRING));
  PyDict_SetItemString(d, "NPY_UNICODE", PyInt_FromLong(NPY_UNICODE));
  PyDict_SetItemString(d, "NPY_VOID", PyInt_FromLong(NPY_VOID));
  PyDict_SetItemString(d, "NPY_NTYPES", PyInt_FromLong(NPY_NTYPES));
  PyDict_SetItemString(d, "NPY_NOTYPE", PyInt_FromLong(NPY_NOTYPE));
  PyDict_SetItemString(d, "NPY_USERDEF", PyInt_FromLong(NPY_USERDEF));

  PyDict_SetItemString(d, "CONTIGUOUS", PyInt_FromLong(NPY_ARRAY_C_CONTIGUOUS));
  PyDict_SetItemString(d, "FORTRAN", PyInt_FromLong(NPY_ARRAY_F_CONTIGUOUS));
  PyDict_SetItemString(d, "OWNDATA", PyInt_FromLong(NPY_ARRAY_OWNDATA));
  PyDict_SetItemString(d, "FORCECAST", PyInt_FromLong(NPY_ARRAY_FORCECAST));
  PyDict_SetItemString(d, "ENSURECOPY", PyInt_FromLong(NPY_ARRAY_ENSURECOPY));
  PyDict_SetItemString(d, "ENSUREARRAY", PyInt_FromLong(NPY_ARRAY_ENSUREARRAY));
  PyDict_SetItemString(d, "ALIGNED", PyInt_FromLong(NPY_ARRAY_ALIGNED));
  PyDict_SetItemString(d, "WRITEABLE", PyInt_FromLong(NPY_ARRAY_WRITEABLE));
  PyDict_SetItemString(d, "UPDATEIFCOPY", PyInt_FromLong(NPY_ARRAY_UPDATEIFCOPY));
  PyDict_SetItemString(d, "WRITEBACKIFCOPY", PyInt_FromLong(NPY_ARRAY_WRITEBACKIFCOPY));

  PyDict_SetItemString(d, "BEHAVED", PyInt_FromLong(NPY_ARRAY_BEHAVED));
  PyDict_SetItemString(d, "BEHAVED_NS", PyInt_FromLong(NPY_ARRAY_BEHAVED_NS));
  PyDict_SetItemString(d, "CARRAY", PyInt_FromLong(NPY_ARRAY_CARRAY));
  PyDict_SetItemString(d, "FARRAY", PyInt_FromLong(NPY_ARRAY_FARRAY));
  PyDict_SetItemString(d, "CARRAY_RO", PyInt_FromLong(NPY_ARRAY_CARRAY_RO));
  PyDict_SetItemString(d, "FARRAY_RO", PyInt_FromLong(NPY_ARRAY_FARRAY_RO));
  PyDict_SetItemString(d, "DEFAULT", PyInt_FromLong(NPY_ARRAY_DEFAULT));
  PyDict_SetItemString(d, "UPDATE_ALL", PyInt_FromLong(NPY_ARRAY_UPDATE_ALL));

  if (PyErr_Occurred())
    Py_FatalError("can't initialize module wrap");

#ifdef F2PY_REPORT_ATEXIT
  on_exit(f2py_report_on_exit,(void*)"array_from_pyobj.wrap.call");
#endif

  return RETVAL;
}
#ifdef __cplusplus
}
#endif
